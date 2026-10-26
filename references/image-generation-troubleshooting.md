# Codex image-generation requirements and diagnostics

[Korean](image-generation-troubleshooting.ko.md)

Applies to native PNG/JPG generation. The plugin supplies instructions, not an image service or account entitlement.

## Account and session

- **Codex Free plan:** native image generation is not available. Free Codex coding or ChatGPT web images do not imply Codex image access. See the official [pricing FAQ](https://developers.openai.com/codex/pricing/).
- **Eligible ChatGPT sign-in:** the native path does not require `OPENAI_API_KEY`. Usage limits and workspace policy still apply. Do not change login or request a key merely because a tool is absent.
- **Provider/model:** the native tool requires the image-generation feature, an image-capable provider/model and Codex-backend authorization. API-key-only login is a separate route; adding a key does not enable the missing native tool. See the pinned [availability gate](https://github.com/openai/codex/blob/rust-v0.162.0/codex-rs/core/src/tools/spec_plan.rs) and [auth modes](https://github.com/openai/codex/blob/rust-v0.162.0/codex-rs/protocol/src/auth.rs).
- **Actual inventory:** include deferred tools. `image_generation` is the feature flag; `image_gen` is a namespace. A session may expose `image_gen__imagegen`; use the actual native tool name rather than declaring it absent on a literal-name mismatch.

Windows and `codex exec` are not categorically excluded. Native Windows `codex exec` generation was verified on a separate, non-Free test account with a ChatGPT-authenticated app-bundled CLI `0.164.0-alpha.11.1` ([runtime evidence](../records/2026-10-26-issue-1-investigation.md)); this does not prove the reporter's result or Free-account support. `0.162.0` source also contains the tool. These are checked versions, **not a proven minimum version**. App builds and CLI versions are different identifiers.

## Windows installation

Run in the same PowerShell terminal where the problem occurs:

```powershell
Get-Command codex -All
where.exe codex
codex --version
```

If `codex` is not found, that terminal cannot invoke it even if the desktop app is installed. Install CLI using the official [CLI installation instructions](https://github.com/openai/codex#installing-and-running-codex-cli), reopen the terminal and repeat. The plugin installer installs/registers this plugin, not Codex CLI. The documented npm option can be invoked on Windows as `npm.cmd install -g @openai/codex`; Node/npm must already be available.

For diagnosis without a separate installation, a Microsoft Store app may bundle a CLI:

```powershell
$app = Get-AppxPackage OpenAI.Codex | Select-Object -First 1
if (-not $app) { throw "Codex Store package not found; use the official CLI install instructions." }
$cli = Join-Path $app.InstallLocation 'app\resources\codex.exe'
if (-not (Test-Path $cli)) { throw "Bundled CLI path differs; use the official CLI install instructions." }
& $cli --version
& $cli login status
& $cli features list | Select-String 'image_generation'
```

Use `resources\codex.exe`, not the GUI `Codex.exe`. This layout was observed on the test machine, not guaranteed for every installation. Do not hard-code its versioned WindowsApps path. In subsequent commands replace `codex` with `& $cli` when diagnosing this executable.

If `codex exec` already completed, a runnable CLI existed in that invocation. Missing PATH in another terminal is not proof of its cause. Compare executable paths and versions, and distinguish native Windows, WSL and the desktop's bundled CLI.

## Missing-tool recovery

Capture non-secret diagnostics:

```powershell
codex --version
codex login status
codex features list | Select-String 'image_generation'
codex plugin list
```

Use `grep image_generation` in a POSIX shell. Check the plan in the account/usage UI and the selected model/provider. Never paste tokens, `auth.json`, API keys or full private configuration.

1. Confirm which binary ran and whether login is ChatGPT or API-key-only. Record the plan only if observed. If Free, explain the documented Codex image restriction.
2. If `image_generation` is listed but false, test one invocation with `codex exec --enable image_generation "Report whether the native image tool is exposed; do not generate an image."`. This does not override account/provider/model restrictions. If the flag is unknown, update the relevant CLI using its official install method instead of inventing a setting.
3. If the flag is true but the tool is absent, check plan, provider/model and workspace policy. Update the relevant Codex client if needed, verify the plugin version and start a new task after updating. Plugin reinstall alone does not grant host capabilities.
4. If the tool exists but its call fails, preserve the exact error and distinguish auth/access denial, usage/rate limits and filesystem/sandbox failures. Do not relabel every failure as a missing tool. A source can exist under `$CODEX_HOME/generated_images/` (default `~/.codex/generated_images/`) even if workspace copying is denied; report generation and copy/finishing separately.
5. If unresolved, report invocation, app/CLI versions separately, login method, observed or unknown plan, feature value, model/provider, actual tool name or absence, and exact error. Do not infer the reporter's account from a different test machine.

Stop before paid fallback. The installed imagegen skill's CLI/API fallback requires a key and explicit user choice, with separate API billing. Browser generation is also only an explicit alternative. Do not execute either automatically or require upgrading as the only next step. Recommendations and processing user-provided source files can remain within scope without native generation.
