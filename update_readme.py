import requests
import re
from datetime import datetime

def fetch_devto(top_n=5):
    """Fetch top Dev.to articles"""
    url = f"https://dev.to/api/articles?top=1&per_page={top_n}"
    articles = requests.get(url, timeout=10).json()

    topics = []
    for article in articles:
        title = article.get("title", "No title")
        link = article.get("url", "")
        topics.append(f"- [{title}]({link})")
    return topics

def update_readme(topics):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Update trending topics section
    new_section = (
        "## 🔥 Trending Tech Topics (Auto-updated daily)\n"
        "<!-- START_TRENDING -->\n"
        + "\n".join(topics)
        + "\n<!-- END_TRENDING -->"
    )
    content = re.sub(
        r"## 🔥 Trending Tech Topics.*<!-- END_TRENDING -->",
        new_section,
        content,
        flags=re.S,
    )

    # Update last updated timestamp
    today = datetime.utcnow().strftime("%b %d, %Y")
    content = re.sub(
        r"<!-- LAST_UPDATED -->.*<!-- END_LAST_UPDATED -->",
        f"<!-- LAST_UPDATED -->{today}<!-- END_LAST_UPDATED -->",
        content,
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    devto_topics = fetch_devto(5)
    update_readme(devto_topics)
