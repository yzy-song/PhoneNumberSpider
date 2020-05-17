# -*- coding: utf-8 -*-
import scrapy
from PhoneNumberSpider.items import PhonenumberspiderItem


class JobCitiesSpider(scrapy.Spider):
    name = 'job_cities'
    allowed_domains = ['dianhua.mapbar.com']
    start_urls = [
        'http://dianhua.mapbar.com/',
    ]

    # 爬取的方法
    def parse(self, response):

        # 注意在上面导入PhonenumberspiderItem包
        item = PhonenumberspiderItem()
        # 匹配
        for jobs_primary in response.xpath('//div[@class="phonenum clr"]'):

            province_name = jobs_primary.xpath(
                './div[@class="ptitle"]/h2/text()').extract()

            city_name = jobs_primary.xpath(
                './div[@class="column"]/dl/dt/a/text()').extract()

            city_link_arr = jobs_primary.xpath(
                './div[@class="column"]/dl/dt/a/@href').extract()

            item['province'] = province_name[0].replace('电话区号', '')

            for index in range(len(city_link_arr)):

                if city_name[index]:
                    item['city'] = city_name[index]
                    yield scrapy.Request(city_link_arr[index] + 'C03', meta={'item': item, 'idx': index}, callback=self.parse_page)

    def parse_page(self, response):
        # 解析1个城市的页面

        item = response.meta['item']
        print(item)
        yield item
