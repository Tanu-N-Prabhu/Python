import requests
import re

# Fetch trending repos (unofficial API)
url = "https://ghapi.huchen.dev/repositories?since=daily"
response = requests.get(url).json()

# Get top 5 trending
topics = []
for repo in response[:5]:
    topics.append(f"- [{repo['name']}]({repo['url']}) ⭐ {repo['stars']} stars\n  {repo['description']}")

# Read README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Build new section
new_section = "## 🔥 Trending Tech Topics (Auto-updated daily)\n<!-- START_TRENDING -->\n"
new_section += "\n".join(topics)
new_section += "\n<!-- END_TRENDING -->"

# Replace old section
content = re.sub(
    r"## 🔥 Trending Tech Topics.*<!-- END_TRENDING -->",
    new_section,
    content,
    flags=re.S,
)

# Save updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
