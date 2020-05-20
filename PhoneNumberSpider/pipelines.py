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

        """
        保存为excel文件
        """
        self.line = 1
        self.mypd = xlwt.Workbook(encoding="utf8")
        self.sheet = self.mypd.add_sheet("电话")
        self.sheet.col(0).width = 256 * 20  # Set the column w
        self.sheet.col(1).width = 256 * 20
        self.sheet.col(2).width = 256 * 50
        self.sheet.col(3).width = 256 * 20
        self.sheet.col(4).width = 256 * 20
        self.sheet.col(5).width = 256 * 20

        self.tall_style = xlwt.easyxf('font:height 300')
        first_row = self.sheet.row(0)
        first_row.set_style(self.tall_style)

        head = [
            "省份",
            "城市",
            "单位名称",
            "电话号码",
            "单位分类",
            "分类链接",
        ]
        for h in head:
            self.sheet.write(0, head.index(h), h)

        """
        保存为csv文件
        self.mypd = pd.DataFrame(columns=['name', 'uri', 'date', 'desc'])

        """

    def close_spider(self, spider):  # 重写close_spider回调方法

        """
        保存为excel文件
        """
        self.mypd.save("test2.xls")
        # self.mypd.save("test2.xlsx")
        # self.mypd.save("test2.xlsx")
        # self.mypd.save("test.xlsx")
        # self.mypd.save("cities.xlsx")

        """
        保存为csv文件
        self.mypd.to_csv(self.file_name)
        """

    def process_item(self, item, spider):  # 添加数据到pandas中
        """
        保存为excel文件
        """
        self.sheet.write(self.line, 0, item['province'])
        self.sheet.write(self.line, 1, item['city'])
        self.sheet.write(int(self.line), 2, item['gov_unit_name'])
        self.sheet.write(int(self.line), 3, item['gov_unit_phone'])
        self.sheet.write(int(self.line), 4, item['gov_unit_type'])
        self.sheet.write(int(self.line), 5, item['type_link'])
        self.sheet.row(self.line).set_style(self.tall_style)
        self.line = self.line + 1

        """
        保存为csv文件
        self.mypd = self.mypd.append(
            {'name': item['name'][0], 'uri': item['uri'][0], 'date': item['date'][0], 'desc': item['desc']}, ignore_index=True)
            print(len(self.mypd))
        """

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
