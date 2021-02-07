# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ChannelsPipeline:
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.db = client['single']
        for i in self.db.collection_names():
            self.db[i].drop()

    def process_item(self, item, spider):
        if item['audience'][-1] == 'K':
            item['audience'] = int(float(item['audience'].split('K')[0])*1000)
        if item['type'] == 'cha':
            collection = self.db['games']
            collection.update({'name': item['name']}, {"$set": item}, upsert=True)
        else:
            collection = self.db['channels']
            collection.update({'streamername': item['streamername']}, {"$set": item}, upsert=True)
