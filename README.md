# Countdown Clicker

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-green)

A simple cross-platform tool that displays a full‑screen countdown (5 → 4 → 3 → 2 → 1 → GO) and then automatically performs a left mouse click at the current cursor position.

Perfect for automating a click after a visual delay – for example, before a game round starts or any other timed action.

## Features

- ✅ **Big, clear numbers** – The window covers 90% of the screen and the font size adjusts automatically.
- ✅ **Always on top** – The countdown stays above all other windows.
- ✅ **Semi‑transparent** (`alpha=0.9`) – You can still see what’s behind.
- ✅ **No window borders** – Clean, immersive overlay.
- ✅ **Automatic click** – Simulates a left mouse button click right after “GO”.
- ✅ **Cross‑platform** – Works on **Windows 11** and **Linux** (X11 session required on Linux).

## Requirements

- Python 3.7 or newer
- `pyautogui` (installed automatically via pip)
- `tkinter` – included with standard Python installations
- Linux only: `scrot` and `python3-tk` (see installation notes below)

## Installation

### 1. Clone the repository (or download the script)

```bash
git clone https://github.com/yourusername/countdown-clicker.git
cd countdown-clicker
