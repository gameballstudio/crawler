# scrapy crawl baomoi -o baomoi.json
# scrapy crawl baomoi -o baomoi.csv
# scrapy shell url for texting

import scrapy
from scrapy import Spider
from scrapy.selector import Selector


class CrawlerTaw01Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    cmt = scrapy.Field()
    total = scrapy.Field()
    pass

class Baomoi_Crawler(Spider):
    name = 'baomoi'
    allowed_domains = ['www.baomoi.com']
    start_urls = ['https://baomoi.com/tim-kiem/hang-khong.epi']

    def parse(self, response):
        list_of_titles = Selector(response).xpath('//h4[@class="story__heading"]/a')
        count = len(list_of_titles)
        i = 1
        text = list_of_titles[0]
        lists = text.xpath('//h4/a/text()').getall()
        # for text in list_of_titles:
        #     item = CrawlerTaw01Item()
        #     item['title'] = text.xpath('//h4/a/text()').get()
        #     item['cmt'] = i
        #     item['total'] = count
        #     i = i + 1
        #     yield item
        for tmp in lists:
            item = CrawlerTaw01Item()
            item['title'] = tmp
            item['cmt'] = i
            item['total'] = count
            i = i + 1
            yield item





