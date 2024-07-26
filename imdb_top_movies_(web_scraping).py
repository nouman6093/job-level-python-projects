#this code is gonna make a file which would store top movies of imdb
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250", headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="ipc-title__text")

movies = [i.getText() for i in all_movies]

with open("movies.txt", mode="w") as data:
    for i in movies:
        data.write(f"{i}\n")
