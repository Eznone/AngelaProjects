from bs4 import BeautifulSoup
import requests as req

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
soup = req.get(URL)
html = soup.text

gallery = html.find("div", {"class": "gallery"})
print(gallery)