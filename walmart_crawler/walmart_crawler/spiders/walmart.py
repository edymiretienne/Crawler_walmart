# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider

from walmart_crawler.items import WalmartCrawlerItem

class WalmartSpider(CrawlSpider):
    name = 'walmart'
    allowed_domains = ['www.walmart.com.br']
    start_urls = ['https://www.walmart.com.br/']

    def parse(self, response):
        categories = response.xpath("//dl/dd/a/@href").extract()
        for a in categories:
        	yield scrapy.Request(response.urljoin(a), callback=self.parse_categories)

    def parse_categories(self, response):
        subcategories = response.xpath("//a[@class='left-menu-item']/@href").extract()
        for b in subcategories:
        	yield scrapy.Request(response.urljoin(b), callback=self.parse_subcategories)
        	
    def parse_subcategories(self, response):
        products = response.xpath("//li/section/div[@class='card-price-container']/a/@href").extract()
        for c in products:
            yield scrapy.Request(response.urljoin(c), callback=self.parse_products)
        next_page_url = response.xpath('//div[@class="product-list shelf-multiline"]/a/@href').extract_first()
        yield scrapy.Request(response.urljoin(next_page_url),callback=self.parse_subcategories_aux)

    def parse_subcategories_aux (self, response):
        products = response.xpath("//li/section/div[@class='card-price-container']/a/@href").extract()
        for c in products:
            yield scrapy.Request(response.urljoin(c), callback=self.parse_products)
        next_page_url = response.xpath('//div[@class="product-list shelf-multiline"]/a/@href').extract()[1]
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse_subcategories_aux)

    def parse_products(self, response):
        dimensoes1 = response.xpath("//dd[@class='dimensions-description']/@itemprop").extract()
        dimensoes2 = response.xpath("//dd[@class='dimensions-description']/text()").extract()
        caract1 =response.xpath("//table[@class='characteristics table-striped']/tbody/tr/th/text()").extract()
        caract2 = response.xpath("//table[@class='characteristics table-striped']/tbody/tr/td/text()").extract()
        caracteristicas=[]
        for i in range(0,len(caract1)):
            d={}
            d['name']=caract1[i]
            d['value']=caract2[i]
            caracteristicas.append(d)
        valor_antigo = response.xpath("//p[@class='product-price']/@data-price-old").extract()[0]
        valor_antigo = float(re.sub('\.','',valor_antigo))/100
        imagem_principal = response.xpath("//img[@class='main-picture']/@src").extract()[0]
        imagem_principal = ("https:"+ imagem_principal)
        imagens_secundarias = response.xpath("//img[@class='thumb']/@src").extract()
        for i, item in enumerate(imagens_secundarias):
            imagens_secundarias[i] = ("https:"+item)

        item = WalmartCrawlerItem()
        item['url'] = response.url
        item['nome'] = response.xpath("//h1[@class='product-name']/text()").extract()[0]
        item['descricao'] = response.xpath("//div[@class='description-content']/text()").extract()[0]
        item['categoria'] = response.xpath("//li[@class='breadcrumb-item']/a/span/text()").extract()[0]
        item['marca'] = response.xpath("//a[@class='product-brand']/text()").extract()[0] 
        item['navegacao'] = response.xpath("//li[@class='breadcrumb-item']/a/span/text()").extract()
        item['nome_vendedor'] = response.xpath("//ul[@class='product-sellers-list']/li/@data-seller-name").extract()[0] 
        item['valor'] = float(response.xpath("//ul[@class='product-sellers-list']/li/@data-price").extract()[0])
        item['valor_antigo'] = valor_antigo     
        item['imagem_principal'] = imagem_principal 
        item['imagens_secundarias'] = imagens_secundarias
        item['caracteristicas'] = caracteristicas
        item['dimensoes'] = dict(zip(dimensoes1, dimensoes2))
        
        yield item

