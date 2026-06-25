#!/usr/bin/env python3
import argparse
from pathlib import Path

from PIL import Image
from collections import deque


def parse_hex(value):
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise ValueError("background must be a six-digit hex color")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def within_tolerance(pixel, target, tolerance):
    return all(abs(int(pixel[index]) - target[index]) <= tolerance for index in range(3))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--background", required=True)
    parser.add_argument("--tolerance", type=int, default=0)
    parser.add_argument("--scope", choices=("global", "edge"), default="global")
    parser.add_argument("--enclosed-tolerance", type=int)
    parser.add_argument("--size", type=int)
    parser.add_argument("--dpi", type=int)
    args = parser.parse_args()

    target = parse_hex(args.background)
    image = Image.open(args.input).convert("RGBA")
    if args.size:
        image = image.resize((args.size, args.size), Image.Resampling.LANCZOS)

    pixels = image.load()
    width, height = image.size
    if args.scope == "global":
        remove = bytearray(
            1 if within_tolerance(pixels[x, y][:3], target, args.tolerance) else 0
            for y in range(height)
            for x in range(width)
        )
    else:
        remove = bytearray(width * height)
        queue = deque()

        def enqueue_if_background(x, y):
            index = y * width + x
            if remove[index]:
                return
            r, g, b, _ = pixels[x, y]
            if within_tolerance((r, g, b), target, args.tolerance):
                remove[index] = 1
                queue.append((x, y))

        for x in range(width):
            enqueue_if_background(x, 0)
            enqueue_if_background(x, height - 1)
        for y in range(height):
            enqueue_if_background(0, y)
            enqueue_if_background(width - 1, y)

        while queue:
            x, y = queue.popleft()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < width and 0 <= ny < height:
                    enqueue_if_background(nx, ny)

        enclosed_key_tolerance = (
            args.enclosed_tolerance
            if args.enclosed_tolerance is not None
            else min(args.tolerance, 24)
        )
        for y in range(height):
            for x in range(width):
                index = y * width + x
                if remove[index]:
                    continue
                r, g, b, _ = pixels[x, y]
                if within_tolerance((r, g, b), target, enclosed_key_tolerance):
                    remove[index] = 1

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if remove[y * width + x] or a == 0:
                pixels[x, y] = (0, 0, 0, 0)
            else:
                pixels[x, y] = (r, g, b, 255)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    save_kwargs = {}
    if args.dpi:
        save_kwargs["dpi"] = (args.dpi, args.dpi)
    image.save(output, **save_kwargs)


if __name__ == "__main__":
    main()
