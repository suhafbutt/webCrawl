import pymysql

conn = None


def create_connection():
    if conn is None:
        return pymysql.connect("localhost", "root", "qwerty123")


def create_database():
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS webcrawl;")


def create_table():
    cursor = conn.cursor()
    query = "CREATE  TABLE IF NOT EXISTS `webcrawl`.`news` ( `id` INT  AUTO_INCREMENT PRIMARY KEY ," \
            "`title` VARCHAR(1024) NOT NULL, `subtitle` VARCHAR(1024) , `abstract` VARCHAR(1024) , " \
            "`download_at` DATETIME , `update_at` DATETIME, `url` VARCHAR(1024) );"
    cursor.execute(query)


def add_news(data):
    cursor = conn.cursor()
    does_news_present = does_news_exist(data['url'])
    if does_news_present:
        query = "Update `webcrawl`.`news` set title = %s, subtitle = %s, abstract = %s, update_at = %s " \
                "where url = %s"
        args = (data['headline'], data['headline_intro'], data['article'], data['downloaded_at'], data['url'])
    else:
        query = "INSERT INTO `webcrawl`.`news`(title, subtitle, abstract, download_at, url) " \
                "VALUES(%s,%s, %s, %s, %s)"
        args = (data['headline'], data['headline_intro'], data['article'], data['downloaded_at'], data['url'])

    cursor.execute(query, args)
    conn.commit()


def does_news_exist(url_value):
    cursor = conn.cursor()
    query = "SELECT url FROM webcrawl.news WHERE url=%s"
    args = (url_value)
    cursor.execute(query, args)
    if cursor.fetchone() is not None:
        return True

    return False


def close_connection():
    conn.close()
