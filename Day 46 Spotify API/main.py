from bs4 import BeautifulSoup
import requests as req

userInput = input("What year would you like to travel back to (YYYY-MM-DD):")

#Setup to get website into soup form
URL = f"https://www.billboard.com/charts/hot-100/{userInput}/"
response = req.get(URL)
web_html = response.text
soup = BeautifulSoup(web_html, "html.parser")

moviesList = soup.find_all(name = "h3", id = "title-of-a-story", class_ = "c-title")
movieTitles = [song.getText().strip() for song in moviesList]

print(movieTitles)
