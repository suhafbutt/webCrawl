import news

crawling_url = "https://www.spiegel.de/international/"
news.create_database_connection()
news.create_database_and_table()
fetched_news = news.get_data_from_web(crawling_url)
crawled_data = news.crawl_data(fetched_news)
news.add_data_to_database(crawled_data)
news.close_database_connection()
