import os
import json
import platform
import re
import sys

# Determine the OS
current_os = platform.system()

# Set paths based on the operating system
if current_os == "Darwin":
    # macOS paths
    VSCODE_SETTINGS_DIR = os.path.expanduser("~/Library/Application Support/Code/User")
    PYTHON_SCRIPT_DIR = os.path.expanduser("~/Documents/my_scripts")
    PYTHON_COMMAND = "python3"
    KEYBINDINGS_KEY = "cmd+shift+t"
elif current_os == "Windows":
    # Windows paths
    VSCODE_SETTINGS_DIR = os.path.join(os.getenv('APPDATA'), "Code", "User")
    PYTHON_SCRIPT_DIR = os.path.join(os.getenv('USERPROFILE'), "Documents", "my_scripts")
    PYTHON_COMMAND = "python"
    KEYBINDINGS_KEY = "ctrl+shift+t"
else:
    raise OSError("Unsupported OS")

PYTHON_SCRIPT_NAME = "eng_space_jpn.py"

# Step 1: Create Python script directory if it doesn't exist
print(f"Creating Python script directory at: {PYTHON_SCRIPT_DIR}...")
os.makedirs(PYTHON_SCRIPT_DIR, exist_ok=True)

# Step 2: Write the Python script to the target directory
python_script_content = """
import re
import sys

def add_space_around_english(text):
    # Regex to detect Japanese followed by English/number or English/number followed by Japanese
    mixed_pattern = re.compile(r'([\\u3040-\\u30FF\\u4E00-\\u9FFF])([a-zA-Z0-9])|([a-zA-Z0-9])([\\u3040-\\u30FF\\u4E00-\\u9FFF])')

    # Regex to detect file paths (e.g., /usr/local/bin or C:\\Users\\User\\Documents)
    file_path_pattern = re.compile(r'([a-zA-Z]:\\\\|/)[^\s]*')

    # Regex to detect symbols with Japanese inside and skip them from adding spaces
    inside_symbols_pattern = re.compile(r'[\\(\\{\\[<][^\\(\\{\\[\\]<>{}]*[\\u3040-\\u30FF\\u4E00-\\u9FFF][^\\)\\}\\]>]*[\\)\\}\\]>]')

    # Regex to ensure no spaces are added inside or outside around symbols
    outside_symbols_pattern = re.compile(r'([\\(\\{\\[<])\\s*([^\\)\\}\\]>]+?)\\s*([\\)\\}\\]>])')

    # Regex to handle spaces between Japanese punctuation and English words but ignore for specific punctuation like 「」 and 、
    ignore_japanese_punctuation = re.compile(r'([「」])([a-zA-Z]+)|([a-zA-Z]+)([「」])|([、])([a-zA-Z]+)|([a-zA-Z]+)([、])')

    # Regex to handle spaces outside of symbols when followed or preceded by Japanese characters
    outside_japanese_symbols_pattern = re.compile(r'([\\u3040-\\u30FF\\u4E00-\\u9FFF])([\\(\\{\\[<])|([\\)\\}\\]>])([\\u3040-\\u30FF\\u4E00-\\u9FFF])')

    def add_space(match):
        if match.group(1) and match.group(2):  # Japanese followed by English/number
            return f"{match.group(1)} {match.group(2)}"
        elif match.group(3) and match.group(4):  # English/number followed by Japanese
            return f"{match.group(3)} {match.group(4)}"
        return match.group(0)

    # Step 1: Replace file paths with placeholders
    file_paths = []
    def replace_file_path(match):
        file_paths.append(match.group(0))
        return f"__FILE_PATH_{len(file_paths)}__"

    text = re.sub(file_path_pattern, replace_file_path, text)  # Detect file paths and replace them with placeholders

    # Step 2: Loop until no more changes are made (ensure full formatting)
    previous_text = None
    while previous_text != text:
        previous_text = text

        # Skip adding spaces inside symbols that contain Japanese characters
        text = re.sub(inside_symbols_pattern, lambda m: m.group(0), text)  # Ignore symbols with Japanese inside

        # Apply the pattern to handle spaces between Japanese and English/number
        text = re.sub(mixed_pattern, add_space, text)  # Handle Japanese and English/number

        # Add space outside symbols when followed or preceded by Japanese characters
        text = re.sub(outside_japanese_symbols_pattern, lambda m: f"{m.group(1) or ''} {m.group(2) or m.group(3)} {m.group(4) or ''}".strip(), text)

        # Remove unnecessary spaces inside and around the symbols
        text = re.sub(outside_symbols_pattern, r'\\1\\2\\3', text)

        # Add space between English letters and Japanese punctuation marks but ignore for 「」 and 、
        text = re.sub(ignore_japanese_punctuation, r'\\1\\2\\3\\4\\5\\6\\7\\8', text)

    # Step 3: Restore file paths in the text
    for i, file_path in enumerate(file_paths):
        text = text.replace(f"__FILE_PATH_{i+1}__", file_path)

    return text

def format_file(filepath):
    # Read the file content
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Process the content
    formatted_content = add_space_around_english(content)

    # Write the formatted content back to the file (overwrite)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python eng_space_jpn.py <file_path>")
        sys.exit(1)

    filepath = sys.argv[1]
    format_file(filepath)
    print(f"File '{filepath}' formatted successfully.")
"""

script_file_path = os.path.join(PYTHON_SCRIPT_DIR, PYTHON_SCRIPT_NAME)
with open(script_file_path, 'w') as python_file:
    python_file.write(python_script_content)

print(f"Python script created at: {script_file_path}")

# Step 3: Update VS Code tasks.json to include dynamic home directory
VSCODE_TASKS_FILE = os.path.join(VSCODE_SETTINGS_DIR, "tasks.json")
tasks_content = {
    "version": "2.0.0",
    "tasks": [
        {
            "label": "eng_SPACE_jpn",
            "type": "shell",
            "command": PYTHON_COMMAND,
            "args": [script_file_path, "${file}"],  # Pass the current open file as an argument
            "group": {
                "kind": "build",
                "isDefault": True
            },
            "presentation": {
                "echo": True,
                "reveal": "always",
                "focus": False,
                "panel": "shared"
            },
            "problemMatcher": []
        }
    ]
}

# Handle tasks.json file
if os.path.exists(VSCODE_TASKS_FILE):
    if os.path.getsize(VSCODE_TASKS_FILE) > 0:
        with open(VSCODE_TASKS_FILE, 'r') as file:
            try:
                existing_tasks = json.load(file)
                existing_tasks['tasks'].append(tasks_content['tasks'][0])
            except json.JSONDecodeError:
                print("Error: tasks.json is corrupted. Overwriting with new tasks.")
                existing_tasks = tasks_content
    else:
        print("Tasks file exists but is empty. Overwriting.")
        existing_tasks = tasks_content
else:
    print("Creating VS Code tasks file...")
    os.makedirs(VSCODE_SETTINGS_DIR, exist_ok=True)
    existing_tasks = tasks_content

with open(VSCODE_TASKS_FILE, 'w') as file:
    json.dump(existing_tasks, file, indent=4)

print("VS Code tasks updated.")

# Step 4: Create or update keybindings.json file with updated content
VSCODE_KEYBINDINGS_FILE = os.path.join(VSCODE_SETTINGS_DIR, "keybindings.json")
keybindings_content = [
    {
        "key": KEYBINDINGS_KEY,
        "command": "workbench.action.tasks.runTask",
        "when": "Run Format Text Script"
    }
]

# Handle keybindings file
if os.path.exists(VSCODE_KEYBINDINGS_FILE):
    if os.path.getsize(VSCODE_KEYBINDINGS_FILE) > 0:
        with open(VSCODE_KEYBINDINGS_FILE, 'r') as file:
            try:
                existing_keybindings = json.load(file)
                existing_keybindings.extend(keybindings_content)
            except json.JSONDecodeError:
                print("Error: keybindings.json is corrupted. Overwriting with new keybindings.")
                existing_keybindings = keybindings_content
    else:
        print("Keybindings file exists but is empty. Overwriting.")
        existing_keybindings = keybindings_content
else:
    print("Creating VS Code keybindings file...")
    os.makedirs(VSCODE_SETTINGS_DIR, exist_ok=True)
    existing_keybindings = keybindings_content

with open(VSCODE_KEYBINDINGS_FILE, 'w') as file:
    json.dump(existing_keybindings, file, indent=4)

print("VS Code keybindings updated.")

# Step 5: Notify the user to restart VS Code
print("Setup complete! Please restart VS Code for the changes to take effect.")
