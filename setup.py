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

    def add_space(match):
        if match.group(1) and match.group(2):  # Japanese followed by English/number
            return f"{match.group(1)} {match.group(2)}"
        elif match.group(3) and match.group(4):  # English/number followed by Japanese
            return f"{match.group(3)} {match.group(4)}"
        return match.group(0)

    # Apply the pattern to the entire text
    formatted_text = re.sub(mixed_pattern, add_space, text)

    # Add space between English letters and punctuation marks for better readability
    formatted_text = re.sub(r'([a-zA-Z])([、。])', r'\\1 \\2', formatted_text)
    formatted_text = re.sub(r'([、。])([a-zA-Z])', r'\\1 \\2', formatted_text)

    return formatted_text

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
