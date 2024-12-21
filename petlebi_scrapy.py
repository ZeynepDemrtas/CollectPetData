from scrapy.spiders import Spider
from scrapy import Request
from scrapy.crawler import CrawlerProcess
import json
import os

class SpiderPetlebi(Spider):
    name = 'spider_petlebi'
    start_urls = ['https://www.petlebi.com/kedi-petshop-urunleri',
                'https://www.petlebi.com/kopek-petshop-urunleri',
                'https://www.petlebi.com/kus-petshop-urunleri',
                'https://www.petlebi.com/kemirgen-petshop-urunleri']
    
    def __init__(self):
        self.data = []
    
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def prepare_product_data(self, input_features):
        dict_features = {}
        list_features = input_features.split(',')
        for i in range(len(input_features.split(','))):
            feature_name = list_features[i].split(':')[0].replace('"', '').replace('{', '').replace('}', '')
            try:
                dict_features[feature_name] = list_features[i].split(':')[1].replace('"', '')
            except IndexError: # empty value scenario
                dict_features[feature_name] = ""
        return dict_features

    def parse(self, response):
        product_datas = response.xpath("//div[@class='row listitempage']")
         
        for products in product_datas:
            product_url = products.xpath("./div/div/div/a/@href").extract()
            product_atts = products.xpath("./div/div/div/a/@data-gtm-product").extract()
            product_image = products.xpath("./div/div/div/a/div/div/center/img/@data-original").extract()        

            for i in range(len(product_atts)):
                prepared_product_atts = self.prepare_product_data(product_atts[i])
                self.data.append({'product URL': product_url[i],
                        'product name': prepared_product_atts["name"],
                        'product barcode':'', #int(''),
                        'product price': float(prepared_product_atts["price"]),
                        'product stock': '',
                        'product images': product_image[i],
                        'description': '',
                        'sku': '',
                        'category': prepared_product_atts["category"],
                        'product_id': int(prepared_product_atts['id']),
                        'brand': prepared_product_atts["brand"]
                    })
        
        next_pages = response.xpath("//ul[@class='pagination']/li/a/@href").extract()
        for next_page in next_pages:
            if next_page:
                yield response.follow(next_page, self.parse)
        with open(os.path.abspath(os.getcwd()) + "\petlebi_products.json", "w", encoding="utf-8") as json_file:
            json.dump(self.data, json_file, skipkeys = False, ensure_ascii=False)
        

if __name__ == '__main__':
    obj_crawler = CrawlerProcess()
    obj_crawler.crawl(SpiderPetlebi)
    obj_crawler.start()
    