# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class PhonesPipeline:
    def process_item(self, item, spider):
        return item
class CsvExportPipeline:
    def open_spider(self, spider):
        self.file = open('test.csv', 'w', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['phone_brand', 'phone_model','price','specs'])
        self.items = []

    def close_spider(self, spider):
        # Sort items by phone_model or any other criteria
        self.items.sort(key=lambda x: x['phone_brand'])
        for item in self.items:
            self.writer.writerow([item['phone_brand'], item['phone_model'],item['price'],item['specs'],item['pricing']])
        self.file.close()

    def process_item(self, item, spider):
        self.items.append(item)
        return item
