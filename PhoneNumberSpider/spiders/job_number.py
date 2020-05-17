# -*- coding: utf-8 -*-
import scrapy
from PhoneNumberSpider.items import PhonenumberspiderItem

class JobNumberSpider(scrapy.Spider):
    name = 'job_number'
    allowed_domains = ['dianhua.mapbar.com']
    start_urls = ['http://dianhua.mapbar.com/xingtai/C03']

    def parse(self, response):
        item = PhonenumberspiderItem()

        for jobs_primary in response.xpath('//div/ul/li[@class="clr"]'):

            gov_unit_name = jobs_primary.xpath('./strong/a/text()').extract()
            gov_unit_phone = jobs_primary.xpath('./div/span/text()').extract()

            item['gov_unit_name'] = gov_unit_name
            item['gov_unit_phone'] = gov_unit_phone

            # 再次发送请求获取数据
            # yield scrapy.Request(city_link_arr[index] + 'C03',meta={'idx':index},callback=self.parse_page)
            # yield item

            print(item)
            for index in range(4):
                if index == 0:
                    # print('C03')
                    pass
                else:
                    pass
                    # print('C03_' + str(index))

    def parse_page(self, response):
        # 解析1个城市的页面

        title = response.meta['idx']
        print('index = ' + title)
