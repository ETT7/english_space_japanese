# VS Code Automation for Formatting English and Japanese Text

This project automates the process of adding spaces around English words and numbers when mixed with Japanese text in files open in VS Code. The Python script handles the formatting, and VS Code is configured to run this script with a simple keyboard shortcut.

## Features

- Automatically adds spaces around English phrases and numbers within Japanese text.
- Works seamlessly within VS Code via a custom task.
- Supports both macOS and Windows.

## Behavior

- **Python script (`eng_space_jpn.py`) will be created at:**
  - On macOS: `~/Documents/my_scripts/`
  - On Windows: `C:\\Users\\<Your Username>\\Documents\\my_scripts\\`
  
- **VS Code settings files (`tasks.json` and `keybindings.json`) will be configured in:**
  - On macOS: `~/Library/Application Support/Code/User/`
  - On Windows: `C:\\Users\\<Your Username>\\AppData\\Roaming\\Code\\User\\`

## Requirements

- Python 3 installed on your system.
- VS Code installed on your system.

## Installation

### Step 1: Clone or Download the Project

Clone this repository or download it as a zip file and extract it on your local machine.

### Step 2: Run the Setup Script

Run the provided Python setup script to configure the necessary files and paths.

#### On macOS:

```bash
python3 setup.py
```

#### On Windows:

```bash
python setup.py
```

This script will:

- Create the Python script `eng_space_jpn.py` in the following path:
  - `~/Documents/my_scripts/` (macOS)
  - `C:\\Users\\<Your Username>\\Documents\\my_scripts\\` (Windows)
  
- Configure VS Code `tasks.json` and `keybindings.json` in the following path:
  - `~/Library/Application Support/Code/User/` (macOS)
  - `C:\\Users\\<Your Username>\\AppData\\Roaming\\Code\\User\\` (Windows)

### Step 3: Restart VS Code

After running the setup script, restart VS Code for the changes to take effect.

## Usage

1. Open a file containing mixed Japanese and English text in VS Code.
2. Press `Ctrl + Shift + T` (on Windows) or `Cmd + Shift + T` (on macOS) to run the formatting task.
3. The script will process the open file and automatically format the text.

## Troubleshooting

- **Keybinding issues:** If the keybinding doesn't work, check that your `keybindings.json` and `tasks.json` files were updated correctly:
  - macOS: `~/Library/Application Support/Code/User/`
  - Windows: `C:\\Users\\<Your Username>\\AppData\\Roaming\\Code\\User\\`

- **Python script location:** Ensure the script `eng_space_jpn.py` was created in the `Documents/my_scripts/` folder:
  - macOS: `~/Documents/my_scripts/`
  - Windows: `C:\\Users\\<Your Username>\\Documents\\my_scripts\\`

- **Python not found:** If the script doesn't run, make sure Python 3 is installed and available in your system's path.

## License

This project is licensed under the MIT License.