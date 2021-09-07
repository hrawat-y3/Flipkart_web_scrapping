# Define your item pipelines here


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class FlipPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(#generated connection string to mongodb atlas database in quotes
            'localhost',
             27017)

        db = self.conn[#database name]
        self.collection = db[#collection name]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

