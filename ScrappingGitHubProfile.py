"""
Scrapping GitHub Profile
Web scrapping is one of the most valuable skill every coder should have.
If you want to learn how to collect data from GitHub using web scrapping techniques
"""

"""
When we open any GitHub account, we see a profile picture, the name of the user,
and a short description of the user in the profile section.
Here you will learn how to scrape your GitHub profile image.
For this task, you need some knowledge of HTML and the requests and BeautifulSoup libraries in Python.
"""

import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/sunil456"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
# print(scraper)
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
print(profile_picture)
