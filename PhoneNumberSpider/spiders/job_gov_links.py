# -*- coding: utf-8 -*-
import scrapy
from PhoneNumberSpider.items import PhonenumberspiderItem


class JobGovLinksSpider(scrapy.Spider):
    name = 'job_gov_links'
    allowed_domains = ['dianhua.mapbar.com']
    start_urls = ['http://dianhua.mapbar.com/shijiazhuang']

    nameStrArr = [
        '交通城市管理机构', '政府机关', '直属机构', '法院检察院', '公安局派出所', '省地二级政府', '区县级政府机关',
        '地市级政府机关'
    ]

    # suffixStrArr = ['C01', 'C03', 'C01', 'C30', 'C40', 'CE0', 'CE1', 'CE2']

    def parse(self, response):

        item = PhonenumberspiderItem()

        # /html/body/div[1]/div[2]/div[1]/h1/text()
        # /html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[8]/h3
        # /html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[8]/ul/li[1]/a
        for jobs_primary in response.xpath('//div[@class="tags"]'):
            link_type = jobs_primary.xpath('./h3/text()').extract()

            links = jobs_primary.xpath('./ul/li/a/@href').extract()
            names = jobs_primary.xpath('./ul/li/a/text()').extract()

            city = jobs_primary.xpath('//h1/text()').extract()[0].replace(
                '电话号码大全', '')
            if link_type[0] == '政府机关':
                for index in range(len(links)):
                    # 筛选需要的链接
                    if names[index] in self.nameStrArr and index == 1:

                        item['province'] = '河北'
                        item['city'] = city
                        item['gov_unit_name'] = ''
                        item['gov_unit_phone'] = ''
                        item['gov_unit_type'] = names[index]
                        item['type_link'] = links[index]

                        yield scrapy.Request(links[index],
                                             meta={
                                                 'item': item,
                                                 'idx': index
                                             },
                                             callback=self.parse_gov_type)

                        yield item

    def parse_gov_type(self, response):
        # 解析1个城市的页面

        item = response.meta['item']
        for jobs_primary in response.xpath('//div/ul/li[@class="clr"]'):

            gov_unit_name = jobs_primary.xpath('./strong/a/text()').extract()
            gov_unit_phone = jobs_primary.xpath('./div/span/text()').extract()

            item['gov_unit_name'] = gov_unit_name
            item['gov_unit_phone'] = gov_unit_phone

            # 再次发送请求获取数据
            # /html/body/div[1]/div[2]/div[1]/div[2]/a[2]
            yield scrapy.Request(item['type_link'],callback=self.parse_page)
            yield item


    def parse_page(self, response):
        # 解析1个城市的页面

        item = response.meta['item']
        for jobs_primary in response.xpath('//div/ul/li[@class="clr"]'):

            gov_unit_name = jobs_primary.xpath('./strong/a/text()').extract()
            gov_unit_phone = jobs_primary.xpath('./div/span/text()').extract()

            item['gov_unit_name'] = gov_unit_name
            item['gov_unit_phone'] = gov_unit_phone

            # 再次发送请求获取数据
            yield scrapy.Request(item['type_link'], callback=self.parse_page)
            yield item
