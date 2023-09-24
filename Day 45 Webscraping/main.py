from bs4 import BeautifulSoup
import requests as req

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = req.get(URL)
website_html = response.text

soup =  BeautifulSoup(website_html, "html.parser")

moviesList = soup.find_all(name = "h3", class_ = "title")

movieTitles = []
for movie in moviesList:
    curr = movie.getText()
    movieTitles.append(curr)

movieTitles = movieTitles[::-1]
print(movieTitles)