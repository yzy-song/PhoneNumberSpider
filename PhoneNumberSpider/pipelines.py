# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import xlwt

from scrapy.exceptions import NotConfigured


class PhonenumberspiderPipeline(object):
    def __init__(self, file_name=None):  # 定义构造器，初始化要写入的文件
        if file_name is None:
            raise NotConfigured
        self.file_name = file_name

        # self.mypd = pd.DataFrame(columns=[
        #     'name',
        #     'city_url',
        #     'area_code'
        # ])

        self.line = 1
        self.mypd = xlwt.Workbook(encoding="utf8")
        self.sheet = self.mypd.add_sheet("城市列表")
        self.sheet.col(0).width = 256 * 20  # Set the column w
        self.sheet.col(1).width = 256 * 20
        self.sheet.col(2).width = 256 * 50
        self.sheet.col(3).width = 256 * 20

        self.tall_style = xlwt.easyxf('font:height 300')
        first_row = self.sheet.row(0)
        first_row.set_style(self.tall_style)

        head = ["省份","城市","链接","区号"]
        for h in head:
            self.sheet.write(0,head.index(h),h)

    def close_spider(self, spider):  # 重写close_spider回调方法
        self.mypd.save("cities.xlsx")
        # self.mypd.to_csv(self.file_name)

    def process_item(self, item, spider):  # 添加数据到pandas中
        
        # self.mypd = self.mypd.append(
        #     {
        #         'name': item['name'],
        #         'city_url': item['city_url'],
        #         'area_code': item['area_code']
        #     }, ignore_index=True)

        self.sheet.write(self.line, 0, item['province'])
        self.sheet.write(self.line, 1, item['city'])
        self.sheet.write(int(self.line), 2, item['city_url'])
        self.sheet.write(int(self.line), 3, item['area_code'])
        self.sheet.row(self.line).set_style(self.tall_style)
        self.line = self.line + 1

    def optimizeContent(self,res):
        res = res.replace('b\'', '')
        res = res.replace('\\n', '')
        res = res.replace('\'', '')
        res = res.replace('style', 'nouse')
        res = res.replace('\.', '')
        return res

    @classmethod
    def from_crawler(cls, crawler):
        file_name = crawler.settings.get('FILE_NAME')
        # file_name = scrapy.conf.settings['FILE_NAME'] #这种方式也可以获取到配置
        return cls(file_name)
