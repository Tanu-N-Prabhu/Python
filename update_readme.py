import requests
from bs4 import BeautifulSoup
import re

TRENDING_URL = "https://github.com/trending"

def fetch_trending():
    try:
        html = requests.get(TRENDING_URL, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")

        topics = []
        for repo in soup.find_all("article", class_="Box-row")[:5]:
            # Repo name
            a = repo.find("h2").find("a")
            repo_name = a.text.strip().replace("\n", "").replace(" ", "")
            repo_url = "https://github.com" + a["href"].strip()

            # Description
            desc_tag = repo.find("p")
            desc = desc_tag.text.strip() if desc_tag else "No description."

            # Stars
            stars_tag = repo.find("a", href=re.compile(r"/stargazers"))
            stars = stars_tag.text.strip() if stars_tag else "0"

            topics.append(f"- [{repo_name}]({repo_url}) ⭐ {stars}\n  {desc}")

        return topics
    except Exception as e:
        return [f"- Could not fetch trending repos today (Error: {e})"]

def update_readme(topics):
    # Read current README
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # New section content
    new_section = (
        "## 🔥 Trending Tech Topics (Auto-updated daily)\n"
        "<!-- START_TRENDING -->\n"
        + "\n".join(topics)
        + "\n<!-- END_TRENDING -->"
    )

    # Replace old section
    pattern = r"## 🔥 Trending Tech Topics.*<!-- END_TRENDING -->"
    updated_content = re.sub(pattern, new_section, content, flags=re.S)

    # Save back
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    trending_topics = fetch_trending()
    update_readme(trending_topics)
