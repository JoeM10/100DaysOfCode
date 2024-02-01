from bs4 import BeautifulSoup
import requests

# ---------- NOTES ----------

# with open("website.html") as file:
#   htmlText = file.read()

# soup = BeautifulSoup(htmlText, "html.parser")

# allAnchorTags = soup.find_all(name="a")

# for tag in allAnchorTags:
#   # print(tag.getText())
#   print(tag.get("href"))

# sectionHeading = soup.find(name="h3", class_="heading")
# print(sectionHeading.getText())

# companyURL = soup.select_one(selector="p a")
# print(companyURL)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)

# 
# PROJECT - Get the highest rated article from the website.
# 

response = requests.get("https://news.ycombinator.com/news")
ycWebPage = response.text

soup = BeautifulSoup(ycWebPage, "html.parser")

title = ""
link = ""
score = 0

articles = soup.find_all("span", class_="titleline")

titles = [title.a.getText() for title in articles]
links = [link.a.get("href") for link in articles]

scores = soup.find_all("span", class_="score")
allScores = [int(score.getText().split()[0]) for score in scores]

for article in range(len(articles)):
  if allScores[article-1] > score:
    title = titles[article-1]
    link = links[article-1]
    score = allScores[article-1]

print(f"{title}\n{link}\n{score}")
