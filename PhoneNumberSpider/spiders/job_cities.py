# -*- coding: utf-8 -*-
import scrapy
from PhoneNumberSpider.items import PhonenumberspiderItem


class JobCitiesSpider(scrapy.Spider):
    name = 'job_cities'
    allowed_domains = ['dianhua.mapbar.com']
    start_urls = ['http://dianhua.mapbar.com/']

    # 爬取的方法
    def parse(self, response):
        # 注意在上面导入PhonenumberspiderItem包
        item = PhonenumberspiderItem()
        # 匹配
        for jobs_primary in response.xpath('//div[@class="phonenum clr"]'):
            
            city_name = jobs_primary.xpath('./div[@class="column"]/dl/dt/a/text()').extract()
            
            link_arr = jobs_primary.xpath('./div[@class="column"]/dl/dt/a/@href').extract()

            area_code = jobs_primary.xpath('./div[@class="column"]/dl/dd/text()').extract()

            for index in range(len(link_arr)):
                if city_name[index]:
                    item['name'] = city_name[index]

                if link_arr[index]:
                    item['city_url'] = link_arr[index]
                
                if area_code[index]:
                    item['area_code'] = area_code[index]
                yield item

                # 不能使用return
