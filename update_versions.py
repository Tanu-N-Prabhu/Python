import subprocess
import re

VERSION_FILE = "VERSION_HISTORY.md"

def get_logged_versions():
    """Return a list of already logged commit messages"""
    try:
        with open(VERSION_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        # Extract commit messages from the table
        return re.findall(r"\| [\d\.]+ \| (.+?) \|", content)
    except FileNotFoundError:
        return []

def get_new_commits():
    """Get commits that are not yet in VERSION_HISTORY.md"""
    try:
        result = subprocess.run(
            ["git", "log", "--pretty=%s"], capture_output=True, text=True, check=True
        )
        all_commits = result.stdout.strip().split("\n")
        logged = get_logged_versions()
        # Only return commits not already logged, newest first
        return [c for c in all_commits if c not in logged]
    except Exception as e:
        return []

def get_latest_version():
    """Get the latest version number from file"""
    try:
        with open(VERSION_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.findall(r"^\| (\d+\.\d+\.\d+) \|", content, re.M)
        if match:
            return match[0]  # top-most row is latest
    except FileNotFoundError:
        return None
    return None

def increment_version(version, count=1):
    """Increment patch number by count"""
    if version is None:
        return f"1.0.{count}"
    major, minor, patch = map(int, version.split("."))
    patch += count
    return f"{major}.{minor}.{patch}"

def update_version_history():
    new_commits = get_new_commits()
    if not new_commits:
        print("No new commits to log.")
        return

    latest_version = get_latest_version()
    try:
        with open(VERSION_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = "# Version History\n\n<!-- START_VERSION_HISTORY -->\n| Version | Commit Message |\n|---------|----------------|\n<!-- END_VERSION_HISTORY -->"

    # Add new commits to the top
    for i, commit_msg in enumerate(reversed(new_commits), start=1):
        new_version = increment_version(latest_version, i)
        new_line = f"| {new_version} | {commit_msg} |"
        # Insert after table header
        content = re.sub(
            r"(\| Version \| Commit Message \|\n\|[-| ]+\|[-| ]+\|)",
            rf"\1\n{new_line}",
            content,
            flags=re.S
        )

    with open(VERSION_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Logged {len(new_commits)} new commit(s).")

if __name__ == "__main__":
    update_version_history()
