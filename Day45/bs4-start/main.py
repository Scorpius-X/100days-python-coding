from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

spans = soup.find_all(name= "span", class_ = "titleline")
anchor_score = soup.find_all(name= "span", class_ = "score")

article_texts = []
article_links = []
score_votes = []

for span in spans:
    anchor = span.find("a")
    anchor_text = anchor.get_text()
    article_texts.append(anchor_text)
    anchor_link = anchor.get("href")
    article_links.append(anchor_link)

for score in anchor_score:
    upvotes = int(score.get_text().split()[0])
    score_votes.append(upvotes)

largest_number = max(score_votes)
largest_index = score_votes.index(largest_number)

print(f"title: {article_texts[largest_index]}, link: {article_links[largest_index]}, upvotes:  {largest_number}")











# with open("Day45/bs4-start/website.html") as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, "html.parser")
# # all_anchor_tags = soup.find_all(name= "a")
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))

# #to find a specific tag such as the heading tag, using id

# heading = soup.find(name= "h1", id = "name")
# section_heading = soup.find(name= "h3", class_= "heading")

# #to select by id or class or even the css selector, the pound sign indicates an id selector
# name = soup.select_one(selector= "#name")

# #to select all the tags with a class named heading
# headings = soup.select(".heading")
# print(headings)

# print(heading)
# print(section_heading)
# print(name)