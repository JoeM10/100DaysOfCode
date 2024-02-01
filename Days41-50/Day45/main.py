from bs4 import BeautifulSoup
import requests

# PROJECT - Scrapes the Top 100 movies from the website and prints them in order from 1-100.

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webPage = response.text

soup = BeautifulSoup(webPage, "html.parser")

movies = soup.find("div", class_="gallery")

movieTitlesBackward = [str(movie.h3.getText()) for movie in movies.find_all("div", class_="article-title-description")]
print(movieTitlesBackward)
movieTitlesForward = movieTitlesBackward[::-1]
for movie in movieTitlesForward:
  print(f"{movie}\n")
