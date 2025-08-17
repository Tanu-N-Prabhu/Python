import requests
import re

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

    new_section = (
        "## 🔥 Trending Tech Topics (Auto-updated daily)\n"
        "<!-- START_TRENDING -->\n"
        + "\n".join(topics)
        + "\n<!-- END_TRENDING -->"
    )

    pattern = r"## 🔥 Trending Tech Topics.*<!-- END_TRENDING -->"
    updated_content = re.sub(pattern, new_section, content, flags=re.S)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    devto_topics = fetch_devto(5)   # Only Dev.to, no Hacker News
    update_readme(devto_topics)
