# -*- coding: utf-8 -*-
import scrapy
from house.items import HouseItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['https://hz.lianjia.com/ershoufang/']
    start_urls = ['https://hz.lianjia.com/ershoufang/pg1/']
    for i in range(2,101):
        start_urls.append('https://hz.lianjia.com/ershoufang/pg' + str(i))

    def parse(self, response):
        for each in response.xpath('//li[@class="clear LOGCLICKDATA"]'):
            item = HouseItem()
            item['title'] = each.xpath('./div[1]/div[1]/a/text()').extract()[0]
            item['address'] = each.xpath('./div[1]/div[2]/div/a/text()').extract()[0]
            house_info = each.xpath('./div[1]/div[2]/div/text()').extract()[0].split('|')
            item['type'] = house_info[1].strip()
            item['size'] = house_info[2].strip()
            item['orientation'] = house_info[3].strip()
            item['fitment'] = house_info[4].strip()
            item['price'] = each.xpath('./div[1]/div[6]/div[1]/span/text()').extract()[0]
            yield item
            
            
            
            
