from .Driver.MongoDB import MongoDB


class Scrapy:
    def __init__(self, username, password, host, port=27017, db_driver="MongoDB"):
        if db_driver is "MongoDB":
            self.client = MongoDB(username, password, host, port)
        self.db = self.client.scrapy

    def find(self, collection, query=None, option=None):
        if option is not None:
            return self.db.get_collection(collection).find(query, option)
        else:
            return self.db.get_collection(collection).find(query)
