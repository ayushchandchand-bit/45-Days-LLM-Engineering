# 🐍 Python Installation Guide — Windows · macOS · Linux

A step-by-step setup guide for **complete beginners**. Follow the section for **your** operating
system, then do the **"Verify"** and **"Virtual environments"** steps at the end — those are the
same for everyone.

> **Which version?** Install **Python 3.10 or newer** (this course uses **3.12**). Avoid Python 2
> — it's dead. Avoid the very newest release in its first month (some libraries lag); 3.11/3.12 is
> the sweet spot.

**Time needed:** ~15 minutes. **Cost:** ₹0.

---

## Jump to your OS
- [🪟 Windows](#-windows)
- [🍎 macOS](#-macos)
- [🐧 Linux](#-linux)
- [✅ Verify it works](#-verify-it-works-all-platforms) · [📦 pip](#-pip--installing-packages) · [🧪 Virtual environments](#-virtual-environments-do-this-for-every-project) · [💻 VS Code](#-vs-code-recommended-editor) · [🆘 Troubleshooting](#-troubleshooting)

---

## 🪟 Windows

### Step 1 — Download
1. Go to **https://www.python.org/downloads/windows/**
2. Click **"Latest Python 3 Release"** → download the **Windows installer (64-bit)**.

### Step 2 — Run the installer (⚠️ the important part)
On the **first screen**, before clicking Install:

- ✅ **CHECK the box "Add python.exe to PATH"** at the bottom. This is the #1 thing beginners
  forget, and it causes the dreaded *"python is not recognized"* error.
- Then click **"Install Now"**.
- If asked, click **"Disable path length limit"** at the end.

> 🛑 **Avoid the Microsoft Store version.** If you type `python` and the Store opens, that's a
> placeholder, not a real install. Use the python.org installer above. (You can turn off the
> placeholder: Settings → Apps → *App execution aliases* → toggle off `python.exe` / `python3.exe`.)

### Step 3 — Verify
Open a **new** PowerShell or Command Prompt window (close any old ones first) and run:

```powershell
python --version
```

You should see something like `Python 3.12.x`.

> **The `py` launcher:** Windows also installs a handy launcher. `py --version` works, and
> `py -3.12` picks a specific version if you have several installed.

---

## 🍎 macOS

> The Python that ships with macOS is old and meant for the system — **don't rely on it**. Install
> your own. Two easy options:

### Option A — Official installer (simplest)
1. Go to **https://www.python.org/downloads/macos/**
2. Download the **macOS 64-bit universal2 installer** (`.pkg`).
3. Open it and click through (Continue → Agree → Install).

### Option B — Homebrew (nice if you'll install other dev tools)
If you don't have Homebrew, install it from **https://brew.sh**, then:

```bash
brew install python@3.12
```

### Verify
Open **Terminal** (Cmd+Space → type "Terminal") and run:

```bash
python3 --version
```

You should see `Python 3.12.x`.

> 📌 On macOS/Linux you usually type **`python3`** and **`pip3`** (not `python`/`pip`). Everything
> below works the same — just add the `3`.

---

## 🐧 Linux

Most Linux distros already include Python 3. Check first:

```bash
python3 --version
```

If it's missing or older than 3.10, install it for your distro:

### Debian / Ubuntu / Mint / WSL
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Need a newer version than your distro ships? Use the **deadsnakes** PPA:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv
```

### Fedora / RHEL / CentOS
```bash
sudo dnf install python3 python3-pip
```

### Arch / Manjaro
```bash
sudo pacman -S python python-pip
```

### Verify
```bash
python3 --version
```

---

## ✅ Verify it works (all platforms)

Run these (use `python` on Windows, `python3` on macOS/Linux):

```bash
# 1. Python is installed and on your PATH
python --version        # Windows
python3 --version       # macOS / Linux

# 2. Open the interactive shell (REPL) and do some math
python                  # or: python3
```

You'll see a `>>>` prompt. Try:

```python
>>> 2 + 2
4
>>> print("Python works! 🎉")
Python works! 🎉
>>> exit()
```

To leave the REPL: type `exit()` and Enter, or press **Ctrl+Z then Enter** (Windows) /
**Ctrl+D** (macOS/Linux).

---

## 📦 pip — installing packages

`pip` is Python's package installer (it comes bundled with Python). Check it:

```bash
pip --version           # Windows
pip3 --version          # macOS / Linux
```

If `pip` isn't found, use the always-works form:

```bash
python -m pip --version     # Windows
python3 -m pip --version    # macOS / Linux
```

Upgrade pip itself (optional but nice):

```bash
python -m pip install --upgrade pip
```

---

## 🧪 Virtual environments (do this for **every** project)

A **virtual environment** (`venv`) is an isolated box of packages for one project, so different
projects don't clash. **Always make one per project.**

```bash
# 1. From inside your project folder, create it (named .venv)
python -m venv .venv          # Windows
python3 -m venv .venv         # macOS / Linux

# 2. Activate it
.venv\Scripts\activate        # Windows (PowerShell / CMD)
source .venv/bin/activate     # macOS / Linux

# 3. You'll see (.venv) at the start of your prompt. Now install packages:
pip install requests

# 4. When done, leave it:
deactivate
```

> 🪟 **Windows PowerShell error** *"running scripts is disabled on this system"* when activating?
> Run this once, then try again:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
> ```

For this course, each project folder will have a `requirements.txt`. Install everything at once with:

```bash
pip install -r requirements.txt
```

> ⚡ **Faster alternative (optional):** [`uv`](https://github.com/astral-sh/uv) is a modern, very
> fast replacement for `pip`/`venv`. Install from the link, then `uv venv` and `uv pip install ...`.
> Stick with built-in `venv` + `pip` if you're new — it's everywhere and always works.

---

## 💻 VS Code (recommended editor)

You can use any editor, but we recommend **Visual Studio Code** (free):

1. Download from **https://code.visualstudio.com/** and install.
2. Open VS Code → **Extensions** (Ctrl+Shift+X) → install the **"Python"** extension by Microsoft.
3. Open your project folder (File → Open Folder).
4. Pick your interpreter: **Ctrl+Shift+P** → *"Python: Select Interpreter"* → choose the one inside
   your `.venv`.
5. Run a file with the ▶ button (top-right) or by right-clicking → *Run Python File in Terminal*.

---

## 🆘 Troubleshooting

| Symptom | Cause | Fix |
|--------|-------|-----|
| `'python' is not recognized` (Windows) | PATH checkbox skipped during install | Re-run the installer → **Modify** → tick **"Add to PATH"**, or reinstall and check the box. Open a **new** terminal after. |
| Typing `python` opens Microsoft Store | Store placeholder is active | Install from python.org; disable the alias in Settings → Apps → *App execution aliases*. |
| `python` shows **2.7.x** (macOS/Linux) | That's the old system Python | Use **`python3`** and **`pip3`** instead. |
| `pip: command not found` | pip not on PATH | Use `python -m pip ...` (Windows) / `python3 -m pip ...` (mac/Linux). |
| `Set-ExecutionPolicy` / scripts disabled (Windows) | PowerShell blocks venv activation | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then activate again. |
| Installed a new version but terminal shows the old one | Old terminal cached the PATH | **Close and reopen** the terminal (or sign out/in). |
| `ModuleNotFoundError` after `pip install` | Installed into a different Python/venv | Make sure your `.venv` is **activated**, then reinstall. |

---

## ✔️ You're ready when…
```bash
python --version     # (or python3)  → shows 3.10+
pip --version        # (or pip3)      → shows a version
```

Both work? 🎉 Head to **[Day 01 →](Day-01-Python-Setup-Variables-and-Data-Types/)** and write your
first program.
