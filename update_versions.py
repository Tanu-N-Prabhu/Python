import subprocess
import re

VERSION_FILE = "VERSION_HISTORY.md"
MAX_COMMITS = 20  # Number of recent commits to include (adjust as needed)

def get_recent_commits(n=MAX_COMMITS):
    """Fetch the last n commits from git, using the first line of each message"""
    try:
        result = subprocess.run(
            ["git", "log", f"-n{n}", "--pretty=%B"], capture_output=True, text=True, check=True
        )
        # Take first line of each commit message
        commits = [c.strip().splitlines()[0] for c in result.stdout.strip().split("\n\n") if c.strip()]
        return commits
    except Exception as e:
        print(f"Error fetching commits: {e}")
        return []

def update_version_history():
    commits = get_recent_commits()
    if not commits:
        print("No commits found.")
        return

    # Load existing content
    try:
        with open(VERSION_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = (
            "# Version History\n\n"
            "<!-- START_VERSION_HISTORY -->\n"
            "| Version | Commit Message |\n"
            "|---------|----------------|\n"
            "<!-- END_VERSION_HISTORY -->"
        )

    # Extract existing versions to determine latest version number
    existing_versions = re.findall(r"^\| (\d+\.\d+\.\d+) \|", content, re.M)
    latest_version = existing_versions[0] if existing_versions else None
    version_counter = 1 if latest_version is None else int(latest_version.split('.')[-1]) + 1

    # Remove duplicates (in case some commits are already logged)
    logged_messages = re.findall(r"\| [\d\.]+ \| (.+?) \|", content)
    new_commits = [c for c in commits if c not in logged_messages]

    if not new_commits:
        print("All commits are already logged.")
        return

    # Add new commits to the top
    for commit_msg in reversed(new_commits):
        new_line = f"| 1.0.{version_counter} | {commit_msg} |"
        content = re.sub(
            r"(\| Version \| Commit Message \|\n\|[-| ]+\|[-| ]+\|)",
            rf"\1\n{new_line}",
            content,
            flags=re.S
        )
        version_counter += 1

    # Write back to file
    with open(VERSION_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Logged {len(new_commits)} new commit(s).")

if __name__ == "__main__":
    update_version_history()
