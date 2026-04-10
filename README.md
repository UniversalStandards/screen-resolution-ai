# Screen Resolution AI Assistant
**v1.0.0 — Civilian Edition | Powered by Claude AI**

> A Windows desktop app that diagnoses and fixes display issues using Claude AI. Describe your problem in plain English — the AI analyzes your system and executes fixes with your approval.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Claude AI](https://img.shields.io/badge/AI-Claude%20claude--opus--4--5-orange)](https://anthropic.com)
[![Windows](https://img.shields.io/badge/Platform-Windows%2010%2F11-lightblue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Quick Start

### Prerequisites
- Windows 10/11 (64-bit)
- Python 3.10+ from https://python.org
- Anthropic API key from https://console.anthropic.com

### Build & Run

```bash
# 1. Clone the repo
git clone https://github.com/UniversalStandards/screen-resolution-ai.git
cd screen-resolution-ai

# 2. Double-click build.bat OR run in terminal:
build.bat

# 3. Run the compiled EXE:
.\dist\ScreenResAI.exe
```

Windows will prompt for admin elevation (required for registry and display driver access).

## Features

| Capability | Implementation |
|---|---|
| Resolution change | `ChangeDisplaySettingsW` (Windows API) |
| Refresh rate change | `ChangeDisplaySettingsW` on frequency |
| DPI / Scaling | Registry write to `HKCU\Control Panel\Desktop` |
| GPU driver restart | `Win+Ctrl+Shift+B` keystroke simulation |
| Font cache flush | Stops/clears/restarts `FontCache` service |
| ClearType toggle | Registry + `SystemParametersInfoW` |
| PowerShell commands | Arbitrary PS1 with `-ExecutionPolicy Bypass` |
| Open Settings pages | `ms-settings:display` URI launch |

## How It Works

1. **Snapshot** — App collects full display info (resolution, refresh rate, GPU, DPI, available modes, monitor topology)
2. **Describe** — You type your problem in plain English
3. **Diagnose** — Claude AI analyzes your snapshot + description, returns a structured JSON action plan
4. **Execute** — Each fix is shown as a card; you click to run individually with full confirmation
5. **Verify** — Snapshot refreshes automatically after each successful fix

## Security
- API key stored locally at `%APPDATA%\ScreenResAI\config.json`
- UAC elevation requested at launch for registry/driver access
- All PowerShell commands shown before execution — you approve each one
- Nothing executes automatically

## File Locations

| Path | Contents |
|---|---|
| `%APPDATA%\ScreenResAI\config.json` | API key + preferences |
| `%APPDATA%\ScreenResAI\assistant.log` | Full debug log |

## License
MIT — see [LICENSE](LICENSE)
