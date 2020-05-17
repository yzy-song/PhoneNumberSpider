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

            province_name = jobs_primary.xpath(
                './div[@class="ptitle"]/h2/text()').extract()

            city_name = jobs_primary.xpath(
                './div[@class="column"]/dl/dt/a/text()').extract()

            city_link_arr = jobs_primary.xpath(
                './div[@class="column"]/dl/dt/a/@href').extract()

            area_code = jobs_primary.xpath(
                './div[@class="column"]/dl/dd/text()').extract()

            item['province'] = province_name[0].replace('电话区号', '')

            for index in range(len(city_link_arr)):

                if city_name[index]:
                    item['city'] = city_name[index]

                if city_link_arr[index]:
                    item['city_url'] = city_link_arr[index]

                if area_code[index]:
                    item['area_code'] = area_code[index]

                # 再次发送请求获取数据
                # yield scrapy.Request(city_link_arr[index] + 'C03',meta={'idx':index},callback=self.parse_page)
                # yield item
                print(city_link_arr[index] + 'C03')
                # 不能使用return

    def parse_page(self, response):
        # 解析1个城市的页面

        # /html/body/div[1]/div[2]/div[1]/div[1]/ul/li[1]/strong/a
        title = response.meta['idx']
        print('index = ' +title)