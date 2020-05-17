# -*- coding: utf-8 -*-
import scrapy
from PhoneNumberSpider.items import PhonenumberspiderItem


class JobGovLinksSpider(scrapy.Spider):
    name = 'job_gov_links'
    allowed_domains = ['dianhua.mapbar.com']
    start_urls = ['http://dianhua.mapbar.com/beijing']

    nameStrArr = [
        '交通城市管理机构', '政府机关', '直属机构', '法院检察院', '公安局派出所', '省地二级政府', '区县级政府机关',
        '地市级政府机关'
    ]

    # suffixStrArr = ['C01', 'C03', 'C01', 'C30', 'C40', 'CE0', 'CE1', 'CE2']

    def parse(self, response):

        item = PhonenumberspiderItem()

        # /html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[8]/h3
        # /html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[8]/ul/li[1]/a
        for jobs_primary in response.xpath('//div[@class="tags"]'):
            link_type = jobs_primary.xpath('./h3/text()').extract()

            links = jobs_primary.xpath('./ul/li/a/@href').extract()
            names = jobs_primary.xpath('./ul/li/a/text()').extract()

            if link_type[0] == '政府机关':
                for index in range(len(links)):
                    # 筛选需要的链接
                    if names[index] in self.nameStrArr and index == 0:
                        item['type_link'] = links[index]
                        item['gov_unit_name'] = links[index]
                        item['gov_unit_phone'] = links[index]

                        # yield scrapy.Request(links[index],
                        #                      meta={
                        #                          'item': item,
                        #                          'idx': index
                        #                      },
                        #                      callback=self.parse_page)
                        yield item

    def parse_page(self, response):
        # 解析1个城市的页面

        item = response.meta['item']
        print(item)
