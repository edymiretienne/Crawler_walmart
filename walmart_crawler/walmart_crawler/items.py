# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class WalmartCrawlerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nome = Field()
    marca = Field()
    navegacao = Field()
    categoria = Field()
    nome_vendedor = Field()
    valor = Field()
    valor_antigo = Field()
    url = Field()
    descricao = Field()
    imagem_principal = Field()
    imagens_secundarias = Field()
    dimensoes = Field()
    caracteristicas = Field()
