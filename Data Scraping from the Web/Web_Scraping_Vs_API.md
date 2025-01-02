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

1. **Blocking** — Worldometer will block if it detects an automated behavior
2. **Incorrect HTML Structure** — The scraper cannot scrape the correct form of data. Check the selectors and their attributes.
3. **Slow Network** — If your internet is slow, then it can cause a delay in fetching the data.

---

## API
An Application Program Interface is an intermediate software that allows applications to talk to each other. For example, your phone’s weather app uses APIs to communicate with this system, providing daily weather updates. We shall use the [World Bank API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api) to access the population data.

```Python

# Requests allows you to send HTTP/1.1 requests extremely easily
import requests

# API endpoint for World Bank population data
url = "http://api.worldbank.org/v2/country/WLD/indicator/SP.POP.TOTL?format=json"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()  
    # Extract population value
    population = data[1][0]["value"]  
    print(f"The World Population is: {population}")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

```

## Explanation
You fetch the data from the API using `requests` and use the `json()` to parse the response and access the first element when the data is returned. This can be done using `data[1][0][“value”]`

---


## Output
Upon executing this program, the result will be `The World Population is: 8061876001`. Unlike web scraping, the execution was quick and never prompted `retrieving data`. This is why I love the API. They make our jobs so much easier and better.

---

## Benefits of Leveraging APIs

1. **Structured Data** — APIs' well-defined formats (JSON, XML, etc.) make their data easy to parse and use.
2. **Reliability** — API formats are less prone to frequent changes than HTML.
3. **Speed** — API data retrieval proved significantly faster than web scraping, as the example above demonstrates.
4. **Regulatory Adherence** — APIs usually include simple terms of service, thus offering better legal protection.
5. **Documentation** — Each available API includes comprehensive documentation. This significantly improves API understanding.
6. **Accessibility** — APIs let you access and use data and services from countless different sources.

For more on real-time API usage, see the article below.

[What is API? Use Case and Benefits](https://konghq.com/blog/learning-center/what-is-api?source=post_page-----c578464d6083--------------------------------)

---

## Limitations of APIs

1. **Restricted Access** — To gain access to certain APIs, you may need to register, purchase API keys, or pay.
2. **Less Flexibility** — Customization may be limited by APIs’ inability to supply all of the data that is displayed on a webpage.
3. **Rate Limits** — The maximum number of queries you may make in a given second, hour, or day is frequently limited by APIs.

---

## Benefits of Web Scraping

1. **Dependency** — Scraping may be the sole choice if there is no API or if the API does not provide the necessary data.
2. **Visibility** — Any information seen on the webpage, including dynamically loaded content, can be captured via scraping.
3. **Access Without Registration** — Often, scraping doesn’t require you to sign up or pay for

---

## Limitations of Web Scraping

1. **Fragility** — When the structure of a website changes, web scraping scripts are prone to breaking.
2. **Legal and Ethical Issues** — Depending on the jurisdiction, scraping may be against local laws or even a website’s terms of service.
3. **Performance Overhead** — Scraping can be resource-intensive and slow because it requires downloading and parsing whole HTML pages.
4. **Error Handling** — It can be difficult to handle edge circumstances, like dynamic JavaScript content.

---

## Opinion
Whenever feasible, use the API if it's available. It is more dependable, quicker, and safer from a legal standpoint. If not then use Web Scraping. To stay out of trouble with the law, review the website’s terms of service. For scripts that are effective and maintainable, use scraping libraries such as `BeautifulSoup`, `Selenium`, or `Scrapy`. Use tools such as `Playwright` or `Selenium` to manage dynamic content. For more information about the law standpoint I would highly recommend you guys read the below-listed article by [Lisa R. Lifshitz](https://www.canadianlawyermag.com/external-contributors/lisa-r.-lifshitz)

[Federal Court Makes Clear: Website Scraping is Illegal](https://www.canadianlawyermag.com/news/opinion/federal-court-makes-clear-website-scraping-is-illegal/276128?source=post_page-----c578464d6083--------------------------------)

---

## Conclusion
For population data, APIs such as the World Bank API are more reliable and efficient than scraping the [Worldometer](https://www.worldometers.info/world-population/), which should only be used as a last resort. Prioritize APIs for accurate and dependable data retrieval. I hope you enjoyed reading my article. Suggestions are always welcomed. Until then, see you next time. Happy Writing!
