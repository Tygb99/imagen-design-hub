"""Pre-upload checks for DesignHub elements.

margin   - fail unless the visible subject touches all four edges (PNG or GIF).
crop     - crop a PNG or every GIF frame to the union of visible pixels.
rejected - fail when an upload name matches a previously rejected element.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
import sys

from PIL import Image, ImageSequence

# Alpha at or below this value (out of 255, about 3%) counts as empty canvas.
# Faint shadow or glow pixels this weak are invisible on a white page but still
# widen a plain getbbox() trim, which leaves a visible margin around the subject.
DEFAULT_ALPHA_THRESHOLD = 8
DEFAULT_MIN_SHORT_SIDE = 700
DEFAULT_REJECTED_RECORDS = (
    Path(__file__).resolve().parents[2] / "records" / "designhub-rejected-elements.csv"
)


@dataclass
class Bounds:
    width: int
    height: int
    frames: int
    box: tuple[int, int, int, int] | None

    def margins(self) -> tuple[int, int, int, int]:
        if self.box is None:
            return (self.width, self.height, self.width, self.height)
        left, top, right, bottom = self.box
        return (left, top, self.width - right, self.height - bottom)


def rgba_frames(image: Image.Image) -> list[Image.Image]:
    return [frame.convert("RGBA") for frame in ImageSequence.Iterator(image)]


def visible_box(frames: list[Image.Image], threshold: int) -> tuple[int, int, int, int] | None:
    box = None
    for frame in frames:
        mask = frame.getchannel("A").point([255 if a > threshold else 0 for a in range(256)])
        frame_box = mask.getbbox()
        if frame_box is None:
            continue
        if box is None:
            box = frame_box
        else:
            box = (
                min(box[0], frame_box[0]),
                min(box[1], frame_box[1]),
                max(box[2], frame_box[2]),
                max(box[3], frame_box[3]),
            )
    return box


def measure(path: Path, threshold: int) -> Bounds:
    with Image.open(path) as image:
        frames = rgba_frames(image)
        return Bounds(image.width, image.height, len(frames), visible_box(frames, threshold))


def check_margin(args: argparse.Namespace) -> int:
    failed = 0
    for raw in args.files:
        path = Path(raw)
        bounds = measure(path, args.alpha_threshold)
        left, top, right, bottom = bounds.margins()
        problems = []
        if bounds.box is None:
            problems.append("no visible pixels")
        elif any((left, top, right, bottom)):
            problems.append("transparent margin")
        if min(bounds.width, bounds.height) < args.min_short_side:
            problems.append(f"short side below {args.min_short_side}px")
        status = "FAIL" if problems else "PASS"
        print(
            f"{status} {path} size={bounds.width}x{bounds.height} frames={bounds.frames} "
            f"margin(left,top,right,bottom)=({left},{top},{right},{bottom}) "
            f"alpha>{args.alpha_threshold}"
            + (f" - {', '.join(problems)}" if problems else "")
        )
        failed += bool(problems)
    return 1 if failed else 0


def crop(args: argparse.Namespace) -> int:
    source, destination = Path(args.source), Path(args.destination)
    if destination.exists() and not args.force:
        print(f"Error: output exists: {destination}", file=sys.stderr)
        return 2
    with Image.open(source) as image:
        info = dict(image.info)
        is_gif = image.format == "GIF"
        frames = rgba_frames(image)
        durations = []
        if is_gif:
            for frame in ImageSequence.Iterator(image):
                durations.append(frame.info.get("duration", info.get("duration", 100)))
    box = visible_box(frames, args.alpha_threshold)
    if box is None:
        print(f"Error: no visible pixels in {source}", file=sys.stderr)
        return 1
    cropped = [frame.crop(box) for frame in frames]
    width, height = cropped[0].size
    if min(width, height) < args.min_short_side:
        print(
            f"FAIL {source} cropped size {width}x{height}: short side below "
            f"{args.min_short_side}px. Regenerate larger; do not upscale the crop.",
            file=sys.stderr,
        )
        return 1
    destination.parent.mkdir(parents=True, exist_ok=True)
    if is_gif:
        options = {"save_all": True, "append_images": cropped[1:], "duration": durations, "disposal": 2}
        if "loop" in info:
            options["loop"] = info["loop"]
        cropped[0].save(destination, format="GIF", **options)
    else:
        options = {"dpi": info["dpi"]} if "dpi" in info else {}
        cropped[0].save(destination, format="PNG", **options)
    print(f"Cropped {source} -> {destination} box={box} size={width}x{height} frames={len(cropped)}")
    return 0


def check_rejected(args: argparse.Namespace) -> int:
    with Path(args.records).open(newline="", encoding="utf-8") as handle:
        rejected = {Path(row["fileName"]).stem.lower(): row for row in csv.DictReader(handle)}
    hits = 0
    for raw in args.names:
        row = rejected.get(Path(raw).stem.lower())
        if row is None:
            continue
        hits += 1
        print(
            f"STOP {raw} matches rejected {row['fileName']} "
            f"({row['elementName']}, reason {row['reasonCode']}, rejected {row['rejectedAt']})"
        )
    if hits:
        print(f"{hits} of {len(args.names)} names were rejected before; do not upload them.")
        return 1
    print(f"OK {len(args.names)} names checked against {args.records}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)

    def add_size_options(command: argparse.ArgumentParser) -> None:
        command.add_argument("--alpha-threshold", type=int, default=DEFAULT_ALPHA_THRESHOLD)
        command.add_argument("--min-short-side", type=int, default=DEFAULT_MIN_SHORT_SIDE)

    margin = commands.add_parser("margin", help="Fail when any edge has a transparent margin.")
    margin.add_argument("files", nargs="+")
    add_size_options(margin)
    margin.set_defaults(handler=check_margin)

    cropper = commands.add_parser("crop", help="Crop a PNG or all GIF frames to the visible union.")
    cropper.add_argument("source")
    cropper.add_argument("destination")
    cropper.add_argument("--force", action="store_true")
    add_size_options(cropper)
    cropper.set_defaults(handler=crop)

    rejected = commands.add_parser("rejected", help="Fail when a name matches a rejected element.")
    rejected.add_argument("names", nargs="+", help="Upload file paths or CSV fileName values.")
    rejected.add_argument("--records", default=str(DEFAULT_REJECTED_RECORDS))
    rejected.set_defaults(handler=check_rejected)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    raise SystemExit(args.handler(args))
