import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
hacker_news = BeautifulSoup(response.text, 'html.parser')
title_and_links = hacker_news.select('.storylink')
scores = hacker_news.select('.score')

def create_news_entity( title_and_links, scores):
    news_entities = []
    for idx, item in enumerate(title_and_links):
        title = item.getText()
        link = item.get('href', "")
        points = int(scores[idx].getText().replace(" points",""))
        if points > 100 :
            news_entities.append({
                'title': title,
                'link': link,
                'points': points
            })
    return news_entities

pprint.pprint(create_news_entity(title_and_links, scores))
