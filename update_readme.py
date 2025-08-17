import requests
import re

def fetch_hackernews(top_n=3):
    """Fetch top Hacker News stories"""
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    ids = requests.get(url, timeout=10).json()[:top_n]

    topics = []
    for i in ids:
        story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json", timeout=10).json()
        title = story.get("title", "No title")
        link = story.get("url", f"https://news.ycombinator.com/item?id={i}")
        topics.append(f"- [HN] [{title}]({link})")
    return topics

def fetch_devto(top_n=2):
    """Fetch top Dev.to articles"""
    url = f"https://dev.to/api/articles?top=1&per_page={top_n}"
    articles = requests.get(url, timeout=10).json()

    topics = []
    for article in articles:
        title = article.get("title", "No title")
        link = article.get("url", "")
        username = article.get("user", {}).get("username", "unknown")
        topics.append(f"- [Dev.to] [{title}]({link}) by {username}")
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
    hn_topics = fetch_hackernews(3)
    devto_topics = fetch_devto(2)
    update_readme(hn_topics + devto_topics)
