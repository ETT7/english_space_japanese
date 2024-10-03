
# VS Code Automation for Formatting English and Japanese Text

This project automates the process of adding spaces around English words, numbers, and symbols when mixed with Japanese text in files open in VS Code. The Python script (`eng_space_jpn.py`) handles the formatting, and VS Code is configured to run this script using a simple keyboard shortcut.

---

## Features

- **Automatically adds spaces around English phrases, numbers, and symbols within Japanese text**.
- Works seamlessly within VS Code via a custom task with a keyboard shortcut.
- **Preserves URLs, file paths, and mathematical expressions** without unnecessary changes.
- Supports both **macOS** and **Windows** platforms.
- Adds spaces around Japanese special characters (`。、！？「」`) and adjacent English words or symbols.
- Correctly formats punctuation between Japanese and English, including brackets, parentheses, and other special symbols.

---

## Behavior

- **Python script (`eng_space_jpn.py`)** will be created at:
  - On macOS: `~/Documents/my_scripts/`
  - On Windows: `C:\Users\<Your Username>\Documents\my_scripts\`

- **VS Code settings files (`tasks.json` and `keybindings.json`)** will be configured in:
  - On macOS: `~/Library/Application Support/Code/User/`
  - On Windows: `C:\Users\<Your Username>\AppData\Roaming\Code\User\`

---

## Requirements

- Python 3 installed on your system.
- VS Code installed on your system.

---

## Installation

### Step 1: Clone or Download the Project
Clone this repository or download it as a zip file and extract it on your local machine.

### Step 2: Run the Setup Script
Run the provided Python setup script to configure the necessary files and paths.

- **On macOS**:
  ```bash
  python3 setup.py
  ```

- **On Windows**:
  ```bash
  python setup.py
  ```

This script will:
- Create the Python script `eng_space_jpn.py` in:
  - `~/Documents/my_scripts/` (macOS)
  - `C:\Users\<Your Username>\Documents\my_scripts\` (Windows)
  
- Configure VS Code `tasks.json` and `keybindings.json` in:
  - `~/Library/Application Support/Code/User/` (macOS)
  - `C:\Users\<Your Username>\AppData\Roaming\Code\User/` (Windows)

### Step 3: Restart VS Code
After running the setup script, restart VS Code for the changes to take effect.

---

## Usage

1. **Open a file containing mixed Japanese and English text in VS Code**.
2. Press `Ctrl + Shift + T` (on Windows) or `Cmd + Shift + T` (on macOS) to run the formatting task.
3. The script will process the open file and automatically format the text.

---

## Formatting Behavior

### 1. **Spaces Between Japanese Characters and English Words**
   - Adds spaces between Japanese characters and adjacent English text or numbers.
   - Example:
     - Input: `こんにちはJohnさん`
     - Output: `こんにちは John さん`

### 2. **Handling Symbols Around Japanese and English**
   - Adds spaces between Japanese characters and symbols (e.g., `()`, `[]`, `{}`, `+`, `-`, `*`, `#`, `%`, etc.).
   - Example:
     - Input: `彼は3つのアイテム(+100%増量/#割引)を購入しました。`
     - Output: `彼は 3 つのアイテム (+100% 増量 /# 割引 ) を購入しました。`

### 3. **Japanese Punctuation and English**
   - Adds spaces between Japanese punctuation marks (`、`, `。`, `！`, `？`, `「」`, etc.) and adjacent English text or symbols.
   - Example:
     - Input: `それではまた今度！We’ll keep in touch, right?`
     - Output: `それではまた今度 ！ We’ll keep in touch, right?`

### 4. **Preserving URLs and File Paths**
   - Preserves URLs, file paths, and any text that should remain unformatted.
   - Example:
     - Input: `Please check the path /usr/local/bin and URL https://example.com`
     - Output: `Please check the path /usr/local/bin and URL https://example.com`

### 5. **Brackets and Punctuation Handling**
   - Adds spaces between Japanese punctuation and brackets or parentheses.
   - Example:
     - Input: `これは。[テスト]です`
     - Output: `これは 。 [テスト ]です`

### 6. **Special Handling of Japanese Quotation Marks**
   - Adds spaces between Japanese quotation marks (`「」`, `『』`, etc.) and adjacent English words or symbols.
   - Example:
     - Input: `「さあ行こう！」She is coming soon`
     - Output: `「さあ行こう！」 She is coming soon`

### 7. **Mathematical Expressions**
   - Proper spacing is maintained around mathematical symbols (`+`, `-`, `*`, `/`) and Japanese characters or numbers.
   - Example:
     - Input: `数学では(+3 * 2) - 1 = 5 のような計算を学びます。`
     - Output: `数学では (+3 * 2) - 1 = 5 のような計算を学びます。`

---

## Troubleshooting

- **Keybinding issues**: If the keybinding doesn't work, check that your `keybindings.json` and `tasks.json` files were updated correctly.
  - macOS: `~/Library/Application Support/Code/User/`
  - Windows: `C:\Users\<Your Username>\AppData\Roaming\Code\User/`

- **Python script location**: Ensure the script `eng_space_jpn.py` was created in the `Documents/my_scripts/` folder:
  - macOS: `~/Documents/my_scripts/`
  - Windows: `C:\Users\<Your Username>\Documents\my_scripts\`

- **Python not found**: If the script doesn't run, make sure Python 3 is installed and available in your system's path.

---

## License

This project is licensed under the MIT License.
