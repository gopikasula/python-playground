import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
hacker_news = BeautifulSoup(response.text, 'html.parser')
title_and_links = hacker_news.select('.storylink')
scores = hacker_news.select('.score')

def create_news_entity( title_and_links, scores):
    news_entities = []
    for idx, item in enumerate(title_and_links):
        title = item.getText()
        link = item['href']
        points = scores[idx].getText()
        news_entities.append({
            'title': title,
            'link': link,
            'points': points
        })
    return news_entities

print(create_news_entity(title_and_links, scores))
