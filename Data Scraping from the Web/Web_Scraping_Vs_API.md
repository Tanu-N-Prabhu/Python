# Web Scraping vs API: Which Data Extraction Method is Best for Your Needs?
## Understanding the pros, cons, and best use cases of web scraping and API for data extraction

<p align = "center">
  <img src = "https://github.com/Tanu-N-Prabhu/Python/blob/master/Img/luke-chesser-JKUTrJ4vK00-unsplash.jpg">
</p>
<p align = "center">
Photo by <a href="https://unsplash.com/@lukechesser?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Luke Chesser</a> on <a href="https://unsplash.com/photos/graphs-of-performance-analytics-on-a-laptop-screen-JKUTrJ4vK00?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
</p>

## Problem Statement
Efficiently extracting and using online data is vital in our data-driven world. The two primary data acquisition methods are APIs and web scraping. Web scraping pulls data from websites by parsing HTML, unlike APIs, which provide structured data access directly from the source.

We must analyze, compare, and contrast the two data extraction methods, noting their strengths and weaknesses. This includes a specific analysis of each method’s best use, trustworthiness, performance, legal implications, and restrictions. Furthermore, the task is to build a solution that efficiently, compliantly, and scalably extracts dynamic data (like the current world population) from online sources such as websites and APIs.

---

## Web scraping
Scraping the data from the web is called web scraping. In this approach, we can use the requests to fetch the webpage content and `BeautifulSoup` to parse and extract the content. Let’s use the [Worldometer](https://www.worldometers.info/world-population/) website to get the dynamic population count.

```Python

# Python Libraries used for Web Scraping
import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://www.worldometers.info/world-population/"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
# Don't Run this multiple time, as doing so
# You will send too many request. 
# Will lead to blocking of the site.
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element that contains the world population
    # Sometimes the tags might change keep an eye
    population_element = soup.select_one(".maincounter-number span")
    
    if population_element:
        # Extract and print the population
        population = population_element.text.strip()
        print(f"The Current World Population is : {population}")
    else:
        print("Population data not found.")
else:

    print(f"Failed to retrieve the page. HTTP Status Code: {response.status_code}")

```

## Explanation
You send an HTTP request to the Worldometer website and we use the beautiful soup library to parse and extract the data from the HTML element. This is dynamic data, meaning you will get updated results every time you refresh.

---
## Output
Upon executing this program, you will get the result as `The Current World Population is: 8,196,543,067`. But what I noticed when I executed it on Google Colab I got the output as `Current World Population: retrieving data…` Do you know why is this? Let me know in the comment section.

## Reason
If the program is stuck while executing “retrieving data” it may be because of the following reasons.

1. Blocking — Worldometer will block if it detects an automated behavior
2. Incorrect HTML Structure — The scraper cannot scrape the correct form of data. Check the selectors and their attributes.
3. Slow Network — If your internet is slow, then it can cause a delay in fetching the data.

---
