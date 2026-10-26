# Issue 1: Windows and Free-plan image generation

Date: 2026-10-26. Starting plugin version: 0.7.0, commit `91207a8`.
Issue: [image_gen tool not available](https://github.com/Tygb99/imagen-design-hub/issues/1).

## Scope and conclusion

The reporter used Windows 11, desktop app 26.1013.x and plugin 0.6.2.
Their `codex exec` reached an agent response but no native image tool.
Their account plan, CLI version, provider and model were not supplied.

The investigation used a **separate, already authenticated Windows test machine** over SSH.
Its account claim was `prolite`, not Free. Its desktop app was 26.1021.3705.0
and its app-bundled CLI was 0.164.0-alpha.11.1. These observations do not
establish the original reporter's cause or demonstrate Free-account generation.

Windows `codex exec` can generate native transparent PNGs on this tested
configuration. Free-plan Codex image generation is excluded by the official
pricing FAQ and the version-pinned native-tool registration gate.
The plugin's unconditional API-key-free wording omitted these requirements.
The correction adds conditional requirements and missing-tool diagnostics;
it does not add image entitlement, change authentication or repair a hosted service.

## Hypothesis matrix

| Hypothesis | Verdict | Evidence / limit |
|---|---|---|
| Windows has no CLI because only the desktop app is installed | Context-dependent | On the test machine, PowerShell found no PATH `codex`/`codex.cmd` or npm shim, but the app bundled a working CLI. The reporter's completed `codex exec` already implies a runnable command in that invocation. |
| Windows or `codex exec` categorically lacks native image generation | Refuted | Actual Windows inventory exposed `image_gen__imagegen`; the same CLI generated the inspected PNG below. |
| Free Codex access includes native images | Refuted | Official pricing FAQ explicitly excludes Free; `image_generation_available` returns false for `PlanType::Free` in 0.162.0. Not a live Free-account trial. |
| ChatGPT web Free images imply Codex Free images | Refuted | Separate product capabilities; Codex's specific restriction still applies. |
| Feature disabled | Possible, not established for reporter | 0.162.0 and tested Windows CLI list `image_generation stable true`; deliberately disabling it locally reproduces absence. |
| API-key-only auth or unsupported provider | Possible, not established for reporter | Pinned gate checks provider capability and Codex-backend auth; `AuthMode::ApiKey` is not Codex-backend auth. A fallback asking for a key does not prove the original session used key auth. |
| Model lacks image-input support | Possible, not established for reporter | Pinned gate checks image input modality. |
| Wrong tool-name lookup | Diagnostic risk, not established as cause | `image_generation` is a feature flag, `image_gen` a namespace; actual Windows inventory rendered `image_gen__imagegen`. |
| App/CLI version mismatch, WSL/PATH differences or stale task | Possible, not established for reporter | App build and CLI version differ; capture both and compare the actual invocation. No minimum version was proven. |
| File policy looks like generation failure | Observed adjacent condition | Native source generation succeeded, but the test agent's skill-file read and workspace copy were denied by policy. Source retrieval independently proved generation, not full finishing. |
| Plugin can guarantee image access when installed | Refuted | Plugin instructions do not register the host tool or change account eligibility. |

## Official sources

- [Codex pricing FAQ](https://developers.openai.com/codex/pricing/), image-generation usage section.
- [Codex plan access](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan): general access is distinct from image eligibility.
- [ChatGPT Images](https://help.openai.com/en/articles/11084440-images-in-chatgpt): web access is not Codex entitlement.
- [0.162.0 tool gate](https://github.com/openai/codex/blob/rust-v0.162.0/codex-rs/core/src/tools/spec_plan.rs), `image_generation_available`.
- [0.162.0 feature defaults](https://github.com/openai/codex/blob/rust-v0.162.0/codex-rs/features/src/lib.rs), `ImageGeneration`.
- [0.162.0 auth modes](https://github.com/openai/codex/blob/rust-v0.162.0/codex-rs/protocol/src/auth.rs), `uses_codex_backend`.
- [0.162.0 imagegen skill](https://github.com/openai/codex/blob/rust-v0.162.0/codex-rs/skills/src/assets/samples/imagegen/SKILL.md): native default and explicitly chosen API fallback are different paths.

## Windows runtime evidence

Read-only probes first ran `Get-Command codex,codex.cmd,node,git -All`,
`Get-AppxPackage '*Codex*'`, then invoked the discovered
`app\resources\codex.exe` directly. No CLI install, PATH edit, login change
or plugin reinstall was performed.

The documented package-discovery command was then executed separately:

```powershell
$app = Get-AppxPackage OpenAI.Codex | Select-Object -First 1
$cli = Join-Path $app.InstallLocation 'app\resources\codex.exe'
& $cli --version
& $cli login status
& $cli features list | Select-String 'image_generation'
```

Observed: CLI `0.164.0-alpha.11.1`, ChatGPT login, `image_generation stable true`.
The replay printed `GUIDE_COMMANDS=PASS`; its owned scratch cleanup printed
`DOC_QA_TMP_EXISTS=False`.

Inventory scenario:

```powershell
& $cli exec --ignore-user-config --ephemeral --skip-git-repo-check --sandbox read-only -C $runTmp --json $inventoryPrompt
```

`$inventoryPrompt` prohibited tool calls and requested actual inventory,
not product knowledge. Final response:
`{"image_tool_available":true,"exact_tool_name":"image_gen__imagegen"}`.
The turn completed and the CLI exited 0.

Generation scenario:

```powershell
& $cli exec --ignore-user-config --ephemeral --skip-git-repo-check --sandbox workspace-write -C $runTmp --json $generationPrompt
```

`$generationPrompt` requested exactly one yellow five-point star with a
genuinely transparent background, native `image_gen__imagegen` only, no
browser/API fallback, installs, upload or metadata. It asked to preserve the
returned original. The final response named a source under
`.codex/generated_images/01a176d9-3a1c-7ea2-ba92-296e1a072b74/`.
The agent reported that workspace copying was denied, not that generation failed.

The source was retrieved by SCP, opened visually and measured independently
with Pillow:

| Measurement | Observed |
|---|---|
| Format / mode | PNG / RGBA |
| Dimensions | 1278 x 1230 |
| Bytes | 488242 |
| Alpha extrema | 0, 255 |
| Fully transparent pixels | 1132809 |
| Partial-alpha pixels | 437434 |
| SHA-256 | `6f35017d53cb1d1dd25ac92f32d89e578466aab1b294d4495bfb038e0c9b84d8` |

The star has source margins and rough edges; this is an image-capability
smoke, not an upload-ready DesignHub asset. The original and local evidence
copy are preserved. No full finishing, metadata or upload success is claimed.

## Missing-tool acceptance contract

Only the recovery branch is under acceptance here, not a new full-plugin
installation/productization certification. Existing PNG finishing and CSV code,
existing eval prompts and their expected outputs remain unchanged.

An actual `npm pack --ignore-scripts --pack-destination "$RUN_TMP"` produced
a 62-file package including both new references. The identical archive was
extracted into independent `cold-1/package` and `cold-2/package` directories.
No previous run's generated state was reused.

Each ran:

```sh
codex exec --ignore-user-config --ephemeral --skip-git-repo-check \
  --disable image_generation --disable apps --sandbox read-only \
  -C "$FRESH_PACKAGE" --json --output-last-message "$DURABLE_FINAL" "$PROMPT"
```

The same prompt asked for one transparent PNG star but explicitly designated
a diagnostic run with native generation disabled, bundled-file reads only
and no image/file creation. It requested actual status, evidence boundaries
and executable diagnostic next steps without inferring a plan.

Both actual turns completed with exit 0 and nonzero model usage. Each read
the packaged PNG skill, shared rules and troubleshooting reference, reported
the absent native tool and unknown account conditions, supplied CLI
path/version/login/feature/plugin checks, and initiated no paid or browser fallback.
No image was claimed. Shell reads differed in grouping; the decision, input
files and recovery branch matched. Wording and temporary path may vary.

Before the correction, the same deliberately absent native tool led the
agent only to the installed imagegen skill's API-key fallback explanation,
without this plugin's targeted diagnostic recovery.

## Final verification

After adding explicit Windows provenance, the package contained 63 files.
Two more independent contexts (`cold-3/package`, `cold-4/package`) executed
the same acceptance command and input against that package. Both completed
with exit 0 and nonzero usage; their actual command logs read only the same
three recovery documents. Both returned executable diagnostics without
account inference, image claims or API/browser fallback.

Static verification initially failed because the Windows positive statement
was not linked to the lead's runtime evidence. The separate-account wording,
this record and the actual PNG/hash resolved that evidence gap. The amended
static verification passed; a lead-owned check independently scanned all
nine changed Markdown files: 58 relative links, zero broken targets.

Self-review retained LIGHT scope: existing instructions and references only,
no new production module, auth logic, integration, installer or test changes.
The JPG route already links the shared rules, so its native-tool mention is
not a separate bypass. No executable unit-test script is defined in
`package.json`; this prose change was verified through real agent runs,
actual Windows generation and document/package checks, not prose-pinning tests.

## Boundaries

The reporter's exact account/configuration remains untested. No minimum CLI
version is claimed. Free exclusion is supported by official documentation
and source, not an account switch or a live Free trial.

After the user's explicit request, diagnostic questions were posted in
[comment 6409801245](https://github.com/Tygb99/imagen-design-hub/issues/1#issuecomment-6409801245)
and read back through the GitHub API; the posted body matched the prepared
questions. The comment asks for plan, exact CLI path/version, login method,
feature value, invocation/model/provider and fresh-app-task behavior without
requesting secrets. The reporter's response is not part of this evidence.
Issue closure, push and release were not performed.
