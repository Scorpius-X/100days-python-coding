import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")

movie_titles = soup.find_all(name= "h3", class_= "title")

movie_list = [movie.getText() for movie in movie_titles]
movies = movie_list[::-1]
print(movies)

with open("Day45/bs4-start/movies.txt", "w", encoding= "utf-8") as file:
    for new_list in movies:
        file.write(f"{new_list}\n")