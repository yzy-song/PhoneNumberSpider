# -*- coding: utf-8 -*-
import scrapy
from PhoneNumberSpider.items import PhonenumberspiderItem


class JobGovLinksSpider(scrapy.Spider):
    name = 'job_gov_links'
    allowed_domains = ['dianhua.mapbar.com']
    start_urls = [
        # "http://dianhua.mapbar.com/beijing",
        # "http://dianhua.mapbar.com/shanghai",
        # "http://dianhua.mapbar.com/tianjin",
        # "http://dianhua.mapbar.com/chongqing",
        # "http://dianhua.mapbar.com/handan",
        # "http://dianhua.mapbar.com/shijiazhuang",
        # "http://dianhua.mapbar.com/baoding",
        # "http://dianhua.mapbar.com/zhangjiakou",
        # "http://dianhua.mapbar.com/chengde",
        # "http://dianhua.mapbar.com/tangshan",
        # "http://dianhua.mapbar.com/langfang",
        # "http://dianhua.mapbar.com/cangzhou",
        # "http://dianhua.mapbar.com/hengshui",
        # "http://dianhua.mapbar.com/xingtai",
        # "http://dianhua.mapbar.com/qinhuangdao",
        # "http://dianhua.mapbar.com/shuozhou",
        # "http://dianhua.mapbar.com/xinzhou",
        # "http://dianhua.mapbar.com/taiyuan",
        # "http://dianhua.mapbar.com/datong",
        # "http://dianhua.mapbar.com/yangquan",
        # "http://dianhua.mapbar.com/jinzhong",
        # "http://dianhua.mapbar.com/changzhi",
        # "http://dianhua.mapbar.com/jincheng",
        # "http://dianhua.mapbar.com/linfen",
        # "http://dianhua.mapbar.com/lvliang",
        # "http://dianhua.mapbar.com/yuncheng",
        # "http://dianhua.mapbar.com/hulunbeier",
        # "http://dianhua.mapbar.com/huhehaote",
        # "http://dianhua.mapbar.com/baotou",
        # "http://dianhua.mapbar.com/wuhai",
        # "http://dianhua.mapbar.com/wulanchabu",
        # "http://dianhua.mapbar.com/tongliao",
        # "http://dianhua.mapbar.com/chifeng",
        # "http://dianhua.mapbar.com/eerduosi",
        # "http://dianhua.mapbar.com/bayannaoer",
        # "http://dianhua.mapbar.com/xilinguolemeng",
        # "http://dianhua.mapbar.com/xinganmeng",
        # "http://dianhua.mapbar.com/alashanmeng",
        # "http://dianhua.mapbar.com/shenyang",
        # "http://dianhua.mapbar.com/tieling",
        # "http://dianhua.mapbar.com/dalian",
        # "http://dianhua.mapbar.com/anshan",
        # "http://dianhua.mapbar.com/fushun",
        # "http://dianhua.mapbar.com/benxi",
        # "http://dianhua.mapbar.com/dandong",
        # "http://dianhua.mapbar.com/jinzhou",
        # "http://dianhua.mapbar.com/yingkou",
        # "http://dianhua.mapbar.com/fuxin",
        # "http://dianhua.mapbar.com/liaoyang",
        # "http://dianhua.mapbar.com/chaoyang",
        # "http://dianhua.mapbar.com/panjin",
        # "http://dianhua.mapbar.com/huludao",
        # "http://dianhua.mapbar.com/changchun",
        # "http://dianhua.mapbar.com/jilin",
        # "http://dianhua.mapbar.com/yanbian",
        # "http://dianhua.mapbar.com/siping",
        # "http://dianhua.mapbar.com/tonghua",
        # "http://dianhua.mapbar.com/baicheng",
        # "http://dianhua.mapbar.com/liaoyuan",
        # "http://dianhua.mapbar.com/songyuan",
        # "http://dianhua.mapbar.com/baishan",
        # "http://dianhua.mapbar.com/haerbin",
        # "http://dianhua.mapbar.com/qiqihaer",
        # "http://dianhua.mapbar.com/mudanjiang",
        # "http://dianhua.mapbar.com/jiamusi",
        # "http://dianhua.mapbar.com/suihua",
        # "http://dianhua.mapbar.com/heihe",
        # "http://dianhua.mapbar.com/daxinganling",
        # "http://dianhua.mapbar.com/yichun1",
        # "http://dianhua.mapbar.com/daqing",
        # "http://dianhua.mapbar.com/qitaihe",
        # "http://dianhua.mapbar.com/jixi",
        # "http://dianhua.mapbar.com/hegang",
        # "http://dianhua.mapbar.com/shuangyashan",
        # "http://dianhua.mapbar.com/nanjing",
        # "http://dianhua.mapbar.com/wuxi",
        # "http://dianhua.mapbar.com/zhenjiang",
        # "http://dianhua.mapbar.com/suzhou1",
        # "http://dianhua.mapbar.com/nantong",
        # "http://dianhua.mapbar.com/yangzhou",
        # "http://dianhua.mapbar.com/yancheng",
        # "http://dianhua.mapbar.com/xuzhou",
        # "http://dianhua.mapbar.com/huaian",
        # "http://dianhua.mapbar.com/lianyungang",
        # "http://dianhua.mapbar.com/changzhou",
        # "http://dianhua.mapbar.com/taizhou1",
        # "http://dianhua.mapbar.com/suqian",
        # "http://dianhua.mapbar.com/quzhou",
        # "http://dianhua.mapbar.com/hangzhou",
        # "http://dianhua.mapbar.com/huzhou",
        # "http://dianhua.mapbar.com/jiaxing",
        # "http://dianhua.mapbar.com/ningbo",
        # "http://dianhua.mapbar.com/shaoxing",
        # "http://dianhua.mapbar.com/taizhou2",
        # "http://dianhua.mapbar.com/wenzhou",
        # "http://dianhua.mapbar.com/lishui",
        # "http://dianhua.mapbar.com/jinhua",
        # "http://dianhua.mapbar.com/zhoushan",
        # "http://dianhua.mapbar.com/chuzhou",
        # "http://dianhua.mapbar.com/hefei",
        # "http://dianhua.mapbar.com/bengbu",
        # "http://dianhua.mapbar.com/wuhu",
        # "http://dianhua.mapbar.com/huainan",
        # "http://dianhua.mapbar.com/maanshan",
        # "http://dianhua.mapbar.com/anqing",
        # "http://dianhua.mapbar.com/suzhou2",
        # "http://dianhua.mapbar.com/fuyang",
        # "http://dianhua.mapbar.com/bozhou",
        # "http://dianhua.mapbar.com/huangshan",
        # "http://dianhua.mapbar.com/huaibei",
        # "http://dianhua.mapbar.com/tongling",
        # "http://dianhua.mapbar.com/xuancheng",
        # "http://dianhua.mapbar.com/liuan",
        # "http://dianhua.mapbar.com/chizhou",
        # "http://dianhua.mapbar.com/fuzhou1",
        # "http://dianhua.mapbar.com/xiamen",
        # "http://dianhua.mapbar.com/ningde",
        # "http://dianhua.mapbar.com/putian",
        # "http://dianhua.mapbar.com/quanzhou",
        # "http://dianhua.mapbar.com/zhangzhou",
        # "http://dianhua.mapbar.com/longyan",
        # "http://dianhua.mapbar.com/sanming",
        # "http://dianhua.mapbar.com/nanping",
        # "http://dianhua.mapbar.com/xinyu",
        # "http://dianhua.mapbar.com/nanchang",
        # "http://dianhua.mapbar.com/jiujiang",
        # "http://dianhua.mapbar.com/shangrao",
        # "http://dianhua.mapbar.com/fuzhou2",
        # "http://dianhua.mapbar.com/yichun2",
        # "http://dianhua.mapbar.com/jian",
        # "http://dianhua.mapbar.com/ganzhou",
        # "http://dianhua.mapbar.com/jingdezhen",
        # "http://dianhua.mapbar.com/pingxiang",
        # "http://dianhua.mapbar.com/yingtan",
        "http://dianhua.mapbar.com/heze",
        # "http://dianhua.mapbar.com/jinan",
        # "http://dianhua.mapbar.com/qingdao",
        # "http://dianhua.mapbar.com/zibo",
        # "http://dianhua.mapbar.com/dezhou",
        # "http://dianhua.mapbar.com/yantai",
        # "http://dianhua.mapbar.com/weifang",
        # "http://dianhua.mapbar.com/jining",
        # "http://dianhua.mapbar.com/taian",
        # "http://dianhua.mapbar.com/linyi",
        # "http://dianhua.mapbar.com/binzhou",
        # "http://dianhua.mapbar.com/dongying",
        # "http://dianhua.mapbar.com/weihai",
        # "http://dianhua.mapbar.com/zaozhuang",
        # "http://dianhua.mapbar.com/rizhao",
        # "http://dianhua.mapbar.com/laiwu",
        # "http://dianhua.mapbar.com/liaocheng",
        # "http://dianhua.mapbar.com/shangqiu",
        # "http://dianhua.mapbar.com/zhengzhou",
        # "http://dianhua.mapbar.com/anyang",
        # "http://dianhua.mapbar.com/xinxiang",
        # "http://dianhua.mapbar.com/xuchang",
        # "http://dianhua.mapbar.com/pingdingshan",
        # "http://dianhua.mapbar.com/xinyang",
        # "http://dianhua.mapbar.com/nanyang",
        # "http://dianhua.mapbar.com/kaifeng",
        # "http://dianhua.mapbar.com/luoyang",
        # "http://dianhua.mapbar.com/jiaozuo",
        # "http://dianhua.mapbar.com/jiyuan",
        # "http://dianhua.mapbar.com/hebi",
        # "http://dianhua.mapbar.com/puyang",
        # "http://dianhua.mapbar.com/zhoukou",
        # "http://dianhua.mapbar.com/luohe",
        # "http://dianhua.mapbar.com/zhumadian",
        # "http://dianhua.mapbar.com/sanmenxia",
        # "http://dianhua.mapbar.com/wuhan",
        # "http://dianhua.mapbar.com/xiangyang",
        # "http://dianhua.mapbar.com/ezhou",
        # "http://dianhua.mapbar.com/xiaogan",
        # "http://dianhua.mapbar.com/huanggang",
        # "http://dianhua.mapbar.com/huangshi",
        # "http://dianhua.mapbar.com/xianning",
        # "http://dianhua.mapbar.com/jingzhou",
        # "http://dianhua.mapbar.com/yichang",
        # "http://dianhua.mapbar.com/enshi",
        # "http://dianhua.mapbar.com/shiyan",
        # "http://dianhua.mapbar.com/shennongjia",
        # "http://dianhua.mapbar.com/suizhou",
        # "http://dianhua.mapbar.com/jingmen",
        # "http://dianhua.mapbar.com/xiantao",
        # "http://dianhua.mapbar.com/tianmen",
        # "http://dianhua.mapbar.com/qianjiang",
        # "http://dianhua.mapbar.com/yueyang",
        # "http://dianhua.mapbar.com/changsha",
        # "http://dianhua.mapbar.com/xiangtan",
        # "http://dianhua.mapbar.com/zhuzhou",
        # "http://dianhua.mapbar.com/hengyang",
        # "http://dianhua.mapbar.com/chenzhou",
        # "http://dianhua.mapbar.com/changde",
        # "http://dianhua.mapbar.com/yiyang",
        # "http://dianhua.mapbar.com/loudi",
        # "http://dianhua.mapbar.com/shaoyang",
        # "http://dianhua.mapbar.com/xiangxi",
        # "http://dianhua.mapbar.com/zhangjiajie",
        # "http://dianhua.mapbar.com/huaihua",
        # "http://dianhua.mapbar.com/yongzhou",
        # "http://dianhua.mapbar.com/guangzhou",
        # "http://dianhua.mapbar.com/shanwei",
        # "http://dianhua.mapbar.com/yangjiang",
        # "http://dianhua.mapbar.com/jieyang",
        # "http://dianhua.mapbar.com/maoming",
        # "http://dianhua.mapbar.com/jiangmen",
        # "http://dianhua.mapbar.com/shaoguan",
        # "http://dianhua.mapbar.com/huizhou",
        # "http://dianhua.mapbar.com/meizhou",
        # "http://dianhua.mapbar.com/shantou",
        # "http://dianhua.mapbar.com/shenzhen",
        # "http://dianhua.mapbar.com/zhuhai",
        # "http://dianhua.mapbar.com/foshan",
        # "http://dianhua.mapbar.com/zhaoqing",
        # "http://dianhua.mapbar.com/zhanjiang",
        # "http://dianhua.mapbar.com/zhongshan",
        # "http://dianhua.mapbar.com/heyuan",
        # "http://dianhua.mapbar.com/qingyuan",
        # "http://dianhua.mapbar.com/yunfu",
        # "http://dianhua.mapbar.com/chaozhou",
        # "http://dianhua.mapbar.com/dongguan",
        # "http://dianhua.mapbar.com/fangchenggang",
        # "http://dianhua.mapbar.com/nanning",
        # "http://dianhua.mapbar.com/chongzuo",
        # "http://dianhua.mapbar.com/liuzhou",
        # "http://dianhua.mapbar.com/laibin",
        # "http://dianhua.mapbar.com/guilin",
        # "http://dianhua.mapbar.com/wuzhou",
        # "http://dianhua.mapbar.com/hezhou",
        # "http://dianhua.mapbar.com/yulin2",
        # "http://dianhua.mapbar.com/guigang",
        # "http://dianhua.mapbar.com/baise",
        # "http://dianhua.mapbar.com/qinzhou",
        # "http://dianhua.mapbar.com/hechi",
        # "http://dianhua.mapbar.com/beihai",
        # "http://dianhua.mapbar.com/haikou",
        # "http://dianhua.mapbar.com/qionghai",
        # "http://dianhua.mapbar.com/wenchang",
        # "http://dianhua.mapbar.com/chengmai",
        # "http://dianhua.mapbar.com/baisha",
        # "http://dianhua.mapbar.com/lingshui",
        # "http://dianhua.mapbar.com/baoting",
        # "http://dianhua.mapbar.com/wuzhishan",
        # "http://dianhua.mapbar.com/tunchang",
        # "http://dianhua.mapbar.com/changjiang",
        # "http://dianhua.mapbar.com/qiongzhong",
        # "http://dianhua.mapbar.com/sanya",
        # "http://dianhua.mapbar.com/sansha",
        # "http://dianhua.mapbar.com/danzhou",
        # "http://dianhua.mapbar.com/wanning",
        # "http://dianhua.mapbar.com/dongfang",
        # "http://dianhua.mapbar.com/lingao",
        # "http://dianhua.mapbar.com/ledong",
        # "http://dianhua.mapbar.com/dingan",
        # "http://dianhua.mapbar.com/chengdu",
        # "http://dianhua.mapbar.com/panzhihua",
        # "http://dianhua.mapbar.com/zigong",
        # "http://dianhua.mapbar.com/mianyang",
        # "http://dianhua.mapbar.com/nanchong",
        # "http://dianhua.mapbar.com/dazhou",
        # "http://dianhua.mapbar.com/suining",
        # "http://dianhua.mapbar.com/guangan",
        # "http://dianhua.mapbar.com/bazhong",
        # "http://dianhua.mapbar.com/luzhou",
        # "http://dianhua.mapbar.com/yibin",
        # "http://dianhua.mapbar.com/neijiang",
        # "http://dianhua.mapbar.com/ziyang",
        # "http://dianhua.mapbar.com/leshan",
        # "http://dianhua.mapbar.com/meishan",
        # "http://dianhua.mapbar.com/liangshan",
        # "http://dianhua.mapbar.com/yaan",
        # "http://dianhua.mapbar.com/ganzi",
        # "http://dianhua.mapbar.com/aba",
        # "http://dianhua.mapbar.com/deyang",
        # "http://dianhua.mapbar.com/guangyuan",
        # "http://dianhua.mapbar.com/guiyang",
        # "http://dianhua.mapbar.com/zunyi",
        # "http://dianhua.mapbar.com/anshun",
        # "http://dianhua.mapbar.com/qiannan",
        # "http://dianhua.mapbar.com/qiandongnan",
        # "http://dianhua.mapbar.com/tongren",
        # "http://dianhua.mapbar.com/bijie",
        # "http://dianhua.mapbar.com/liupanshui",
        # "http://dianhua.mapbar.com/qianxinan",
        # "http://dianhua.mapbar.com/xishuangbanna",
        # "http://dianhua.mapbar.com/dehong",
        # "http://dianhua.mapbar.com/zhaotong",
        # "http://dianhua.mapbar.com/kunming",
        # "http://dianhua.mapbar.com/dali",
        # "http://dianhua.mapbar.com/honghe",
        # "http://dianhua.mapbar.com/qujing",
        # "http://dianhua.mapbar.com/baoshan",
        # "http://dianhua.mapbar.com/wenshan",
        # "http://dianhua.mapbar.com/yuxi",
        # "http://dianhua.mapbar.com/chuxiong",
        # "http://dianhua.mapbar.com/puer",
        # "http://dianhua.mapbar.com/lincang",
        # "http://dianhua.mapbar.com/nujiang",
        # "http://dianhua.mapbar.com/diqing",
        # "http://dianhua.mapbar.com/lijiang",
        # "http://dianhua.mapbar.com/lasa",
        # "http://dianhua.mapbar.com/rikaze",
        # "http://dianhua.mapbar.com/shannan",
        # "http://dianhua.mapbar.com/linzhi",
        # "http://dianhua.mapbar.com/changdu",
        # "http://dianhua.mapbar.com/naqu",
        # "http://dianhua.mapbar.com/ali",
        # "http://dianhua.mapbar.com/xian",
        # "http://dianhua.mapbar.com/xianyang",
        # "http://dianhua.mapbar.com/yanan",
        # "http://dianhua.mapbar.com/yulin1",
        # "http://dianhua.mapbar.com/weinan",
        # "http://dianhua.mapbar.com/shangluo",
        # "http://dianhua.mapbar.com/ankang",
        # "http://dianhua.mapbar.com/hanzhong",
        # "http://dianhua.mapbar.com/baoji",
        # "http://dianhua.mapbar.com/tongchuan",
        # "http://dianhua.mapbar.com/linxia",
        # "http://dianhua.mapbar.com/lanzhou",
        # "http://dianhua.mapbar.com/dingxi",
        # "http://dianhua.mapbar.com/pingliang",
        # "http://dianhua.mapbar.com/qingyang",
        # "http://dianhua.mapbar.com/wuwei",
        # "http://dianhua.mapbar.com/jinchang",
        # "http://dianhua.mapbar.com/zhangye",
        # "http://dianhua.mapbar.com/jiuquan",
        # "http://dianhua.mapbar.com/jiayuguan",
        # "http://dianhua.mapbar.com/tianshui",
        # "http://dianhua.mapbar.com/longnan",
        # "http://dianhua.mapbar.com/gannan",
        # "http://dianhua.mapbar.com/baiyin",
        # "http://dianhua.mapbar.com/yinchuan",
        # "http://dianhua.mapbar.com/shizuishan",
        # "http://dianhua.mapbar.com/wuzhong",
        # "http://dianhua.mapbar.com/guyuan",
        # "http://dianhua.mapbar.com/zhongwei",
        # "http://dianhua.mapbar.com/haibei",
        # "http://dianhua.mapbar.com/xining",
        # "http://dianhua.mapbar.com/haidong",
        # "http://dianhua.mapbar.com/huangnan",
        # "http://dianhua.mapbar.com/hainan",
        # "http://dianhua.mapbar.com/guoluo",
        # "http://dianhua.mapbar.com/yushu",
        # "http://dianhua.mapbar.com/haixi",
        # "http://dianhua.mapbar.com/tacheng",
        # "http://dianhua.mapbar.com/hami",
        # "http://dianhua.mapbar.com/hetian",
        # "http://dianhua.mapbar.com/aletai",
        # "http://dianhua.mapbar.com/kezilesu",
        # "http://dianhua.mapbar.com/boertala",
        # "http://dianhua.mapbar.com/kelamayi",
        # "http://dianhua.mapbar.com/wulumuqi",
        # "http://dianhua.mapbar.com/shihezi",
        # "http://dianhua.mapbar.com/changji",
        # "http://dianhua.mapbar.com/wujiaqu",
        # "http://dianhua.mapbar.com/tulufan",
        # "http://dianhua.mapbar.com/bayinguole",
        # "http://dianhua.mapbar.com/akesu",
        # "http://dianhua.mapbar.com/alaer",
        # "http://dianhua.mapbar.com/kashen",
        # "http://dianhua.mapbar.com/tumushuke",
        # "http://dianhua.mapbar.com/yili",
        # "http://dianhua.mapbar.com/hongkong",
        # "http://dianhua.mapbar.com/macau/"
    ]

    nameStrArr = [
        '交通城市管理机构', '政府机关', '直属机构', '法院检察院', '公安局派出所', '省地二级政府', '区县级政府机关',
        '地市级政府机关'
    ]

    exclude_words = [
        "派出所", "法庭", "警务室", "警务处", "街道", "街道办", "街道办事处", "政务中心", "服务中心", "服务站",
        "公证处", "执法大队", "交警大队", "交警支队", "中队", "大队", "接待大厅", "办公室", "工商所", "财政所",
        "稽查所", "镇政府", "镇委", "监测站", "监督站", "监理站", "检验站", "管理站"
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

                        item['province'] = '浙江'
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

            item['type_link'] = new_url

            # 再次发送请求获取数据
            pages = response.xpath('//div[@class="page"]')

            page_num = pages.xpath('./a/text()').extract()
            page_links = pages.xpath('./a/@href').extract()

            now_page = "javascript:void(0);"

            for index in range(len(page_links)):
                if now_page == page_links[index]:
                    if self.check_data(item['gov_unit_name'][0]):
                        print("合法数据：" + item['gov_unit_name'][0])
                        yield item
                else:
                    yield scrapy.Request(page_links[index],meta={'item': item},callback=self.parse_page)



    # 解析1个分类下的单个页面数据
    def parse_page(self, response):

        item = response.meta['item']
        for jobs_primary in response.xpath('//div/ul/li[@class="clr"]'):

            gov_unit_name = jobs_primary.xpath('./strong/a/text()').extract()
            gov_unit_phone = jobs_primary.xpath('./div/span/text()').extract()

            item['gov_unit_name'] = gov_unit_name
            item['gov_unit_phone'] = gov_unit_phone

            # 再次发送请求获取数据
            if self.check_data(item['gov_unit_name'][0]):
                print("合法数据：" + item['gov_unit_name'][0])
                yield item


    # 检测数据是否有用
    def check_data(self,unit_name):
        for index in range(len(self.exclude_words)):
            if unit_name.find(self.exclude_words[index]) >= 0:
                print("非法数据：" + unit_name)
                return False
            else:
                continue

        return True
