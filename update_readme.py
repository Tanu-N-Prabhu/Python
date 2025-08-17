import requests, re

README_PATH = "README.md"
API_URL = "https://dev.to/api/articles?per_page=5"

# Fetch Dev.to trending posts
response = requests.get(API_URL)
articles = response.json()

# Extract top 5 article titles (with links)
topics = [f"- [{a['title']}]({a['url']})" for a in articles[:5]]

with open(README_PATH, "r", encoding="utf-8") as f:
    readme = f.read()

new_section = "### 📈 Trending Tech Topics\n" + "\n".join(topics)

if "### 📈 Trending Tech Topics" in readme:
    # Replace old section with new one
    readme = re.sub(
        r"### 📈 Trending Tech Topics[\s\S]*?(?=###|$)",
        new_section + "\n\n",
        readme,
    )
else:
    # Append section if not present
    readme += "\n" + new_section + "\n"

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(readme)
