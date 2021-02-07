import scrapy
from channels.items import ChannelsItem
import datetime
from selenium import webdriver


class ChannelsspiSpider(scrapy.Spider):
    name = 'channelsSpi'
    allowed_domains = ['twitchtracker.com']
    start_urls = ['https://twitchtracker.com/games']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bro = webdriver.Chrome("chromedriver.exe")

    def parse(self, response):
        yield scrapy.http.Request(url='https://twitchtracker.com/channels/live/english', callback=self.parsest)
        yield scrapy.http.Request(url='https://twitchtracker.com/games', callback=self.parseg)
        for i in range(2, 5):
            yield scrapy.http.Request(url='https://twitchtracker.com/games?page='+str(i), callback=self.parseg)
            yield scrapy.http.Request(url='https://twitchtracker.com/channels/live/english?page='+str(i), callback=self.parsest)

    def parseg(self, response):
        parse_content = response.xpath('//div[@class = "ranked-item"]')
        for i in parse_content:
            item = ChannelsItem()
            item['type'] = 'cha'
            item['timestamp'] = str(datetime.datetime.now().date()) + " " + str(datetime.datetime.now().hour)
            item['name'] = i.xpath('div[3]/a/text()').extract_first()
            item['audience'] = i.xpath('div[4]/div/text()').extract_first()
            print(item)
            yield item

    def parsest(self, response):
        parse_con = response.xpath('//tbody/tr')
        for i in parse_con:
            item = ChannelsItem()
            item['type'] = 'streamer'
            item['timestamp'] = str(datetime.datetime.now().date()) + " " + str(datetime.datetime.now().hour)
            item['streamername'] = i.xpath('td[3]/a/text()').extract_first()
            item['name'] = i.xpath('td[3]/div/text()').extract_first()
            item['audience'] = i.xpath('td[5]/span/text()').extract_first()
            print(item)
            yield item
