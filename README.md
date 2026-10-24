<p align="center">
  <img src="assets/icon.png" width="128" alt="Desktop Pet cat">
</p>

<h1 align="center">Desktop Pet</h1>

<p align="center">
  A little pixel cat that lives on your desktop, walks around, naps, and gives you advice when you click it.
</p>

---

## Features

- 🐱 Walks along the bottom of your screen and turns around at the edges
- 💤 Decides by itself to walk, sit, idle or sleep
- 💬 Click the cat and it gives you a random piece of advice
- 📋 Menu bar / tray icon to make it sit, sleep, walk, give advice or quit
- 🪟 Transparent and always on top, with no window around the cat

## Download

Go to the [**latest release**](https://github.com/Markie-001/desktop-pet/releases/latest) and download the file for your computer:

| Computer | File |
|---|---|
| Windows | `DesktopPet-windows.zip` |
| Mac | `DesktopPet-mac.zip` |

### Windows

1. Right-click `DesktopPet-windows.zip` → **Extract All**.
2. Open the folder and double-click **DesktopPet.exe**.

### Mac

1. Double-click `DesktopPet-mac.zip` to unzip it.
2. Drag **DesktopPet.app** into your **Applications** folder.
3. Double-click it to open.

## ⚠️ About the security warnings

The first time you open the app, Windows or macOS will probably show a warning.
**This is normal for small hobby apps.** It happens because the app is not signed with a paid developer certificate, so your computer doesn't recognize it yet. It does **not** mean the app is harmful. You can read all the code in this repository.

### Windows: "Windows protected your PC"

1. Click **More info**.
2. Click **Run anyway**.

If the app doesn't start at all, Windows Defender may have blocked it by mistake (a "false positive"). Check **Windows Security → Virus & threat protection → Protection history**, and allow DesktopPet there.

### Mac: "DesktopPet Not Opened"

1. Click **Done** (not "Move to Trash").
2. Open **System Settings → Privacy & Security**.
3. Scroll down and click **Open Anyway** next to "DesktopPet was blocked".
4. Enter your password and click **Open**.

Or run this once in the Terminal:

```
xattr -cr /Applications/DesktopPet.app
```

You only need to do this once. After that, the app opens normally.

## How to use

| Action | What happens |
|---|---|
| **Left-click** the cat | The cat gets happy and gives you advice |
| **Right-click** the cat | Quit |
| **Tray / menu bar icon** | Give advice, Sit, Sleep, Walk, Quit |

The advice comes from the internet, so you need a connection. Without it, the cat just says *meow*.

## Run from the code

Needs [Python 3](https://www.python.org/downloads/).

```
git clone https://github.com/Markie-001/desktop-pet.git
cd desktop-pet
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python pet.py
```

## Project files

```
desktop-pet/
├─ pet.py              # the cat: animations, walking, clicks
├─ bubble.py           # the speech bubble
├─ advice.py           # gets advice from the internet
├─ tray.py             # the tray / menu bar icon
├─ assets/
│  ├─ cat.png          # sprite sheet with all the cat pictures
│  └─ icon.png         # app icon
├─ requirements.txt    # Python packages
└─ .github/workflows/
   └─ build.yml        # builds the Windows and Mac apps on GitHub
```

## Built with

- [Python](https://www.python.org/) and [PySide6 (Qt for Python)](https://doc.qt.io/qtforpython-6/)
- [Advice Slip API](https://api.adviceslip.com/) for the advice
- [PyInstaller](https://pyinstaller.org/) and GitHub Actions to build the apps
- Sprites edited in [Piskel](https://www.piskelapp.com/)