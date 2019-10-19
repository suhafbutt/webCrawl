import json
import database
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup


def create_database_connection():
    database.conn = database.create_connection()


def create_database_and_table():
    database.create_database()
    database.create_table()


def get_data_from_web(crawling_url):
    soup = BeautifulSoup(urllib.request.urlopen(crawling_url), "html.parser")
    return soup.findAll("div", {"class": "teaser"})


def crawl_data(news):
    news_data = []
    for n in news:
        news_data.append(
            {
                'headline': json.dumps(n.find("span", {"class": "headline"}).string),
                'headline_intro': json.dumps(n.find("span", {"class": "headline-intro"}).string),
                'article': json.dumps(n.find("p", {"class": "article-intro"}).get_text()),
                'url': n.find("a", {"class": "article-icon"})['href'],
                'downloaded_at': datetime.now()
            }
        )

    return news_data


def add_data_to_database(data):
    for d in data:
        database.add_news(d)


def close_database_connection():
    database.close_connection()
