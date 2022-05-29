# Scrape Table from a Website using Python
"""
There are many Python libraries and modules that you can use for web scraping. To scrape a
table from a website, I will use the urllib module in Python, which is already available in the Python standard library.
"""

import urllib.request
import pandas as pd

url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

with urllib.request.urlopen(url) as i:
    html = i.read()

data = pd.read_html(html)[0]
print(data.head())