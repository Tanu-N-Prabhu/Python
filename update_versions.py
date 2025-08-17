import subprocess
import re

VERSION_FILE = "VERSION_HISTORY.md"

def get_latest_commit_message():
    """Get the latest Git commit message"""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=%s"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Could not fetch commit message ({e})"

def get_latest_version():
    """Get the latest version number from file"""
    try:
        with open(VERSION_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.findall(r"^\| (\d+\.\d+\.\d+) \|", content, re.M)
        if match:
            return match[0]  # latest version is top-most row
    except FileNotFoundError:
        return None
    return None

def increment_version(version):
    """Increment patch number"""
    if version is None:
        return "1.0.0"
    major, minor, patch = map(int, version.split("."))
    patch += 1
    return f"{major}.{minor}.{patch}"

def update_version_history():
    latest_commit = get_latest_commit_message()
    latest_version = get_latest_version()
    new_version = increment_version(latest_version)

    new_line = f"| {new_version} | {latest_commit} |"

    try:
        with open(VERSION_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        # create default placeholder if file missing
        content = "# Version History\n\n<!-- START_VERSION_HISTORY -->\n| Version | Commit Message |\n|---------|----------------|\n<!-- END_VERSION_HISTORY -->"

    # Insert new line after table header
    content = re.sub(
        r"(\| Version \| Commit Message \|\n\|[-| ]+\|[-| ]+\|)",
        rf"\1\n{new_line}",
        content,
        flags=re.S
    )

    with open(VERSION_FILE, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_version_history()
