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

    def parse(self, response):

        item = PhonenumberspiderItem()

        for jobs_primary in response.xpath('//div[@class="tags"]'):
            link_type = jobs_primary.xpath('./h3/text()').extract()

            links = jobs_primary.xpath('./ul/li/a/@href').extract()
            names = jobs_primary.xpath('./ul/li/a/text()').extract()

            city = jobs_primary.xpath('//h1/text()').extract()[0].replace(
                '电话号码大全', '')
            if link_type[0] == '政府机关':
                for index in range(len(links)):
                    # 筛选需要的链接
                    if names[index] in self.nameStrArr:

                        item['province'] = '河北'
                        item['city'] = city
                        item['gov_unit_type'] = names[index]
                        item['type_link'] = links[index]

                        yield scrapy.Request(links[index],
                                             meta={
                                                 'item': item,
                                                 'link': links[index]
                                             },
                                             callback=self.parse_gov_type)


    # 解析1个分类的页面 https://dianhua.mapbar.com/shijiazhuang/C03/
    def parse_gov_type(self, response):

        item = response.meta['item']
        new_url = response.meta['link']

        for jobs_primary in response.xpath('//div/ul/li[@class="clr"]'):

            gov_unit_name = jobs_primary.xpath('./strong/a/text()').extract()
            gov_unit_phone = jobs_primary.xpath('./div/span/text()').extract()

            item['gov_unit_name'] = gov_unit_name
            item['gov_unit_phone'] = gov_unit_phone

            # 再次发送请求获取数据
            pages = response.xpath('//div[@class="page"]')

            page_num = pages.xpath('./a/text()').extract()
            page_links = pages.xpath('./a/@href').extract()

            now_page = "javascript:void(0);"

            for index in range(len(page_links)):
                if now_page == page_links[index]:
                    yield item
                    # yield scrapy.Request(new_url,meta={'item': item},callback=self.parse_page)
                else:
                    yield scrapy.Request(page_links[index],meta={'item': item},callback=self.parse_page)
                    # yield item



    # 解析1个分类下的单个页面数据
    def parse_page(self, response):

        print('parse_page====')
        item = response.meta['item']
        for jobs_primary in response.xpath('//div/ul/li[@class="clr"]'):

            gov_unit_name = jobs_primary.xpath('./strong/a/text()').extract()
            gov_unit_phone = jobs_primary.xpath('./div/span/text()').extract()

            item['gov_unit_name'] = gov_unit_name
            item['gov_unit_phone'] = gov_unit_phone
            # 再次发送请求获取数据
            print('item========')
            yield item
