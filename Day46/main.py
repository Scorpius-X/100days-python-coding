import requests
from bs4 import BeautifulSoup

music_date = input("Which year do you want to travel to? type the date in this format YYYY-MM-DD: ")

web_url = f"https://www.billboard.com/charts/hot-100/{music_date}"
web_header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"}

response = requests.get(url= web_url, headers= web_header)

billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")

