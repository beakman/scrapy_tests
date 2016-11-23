# -*- coding: utf-8 -*-
import scrapy

from jobsbot.items import OfferItem

BASE_URL = 'http://www.milanuncios.com'
KEYWORDS = ['fuengirola',]

class MilanunciosSpider(scrapy.Spider):
    name = "milanuncios"
    allowed_domains = ["milanuncios.com"]
    start_urls = ['http://www.milanuncios.com/ofertas-de-empleo-en-malaga/?dias=1&demanda=n']

    def parse(self, response):
        for oferta in response.xpath('//div[@class="aditem"]'):
            # If title contains any KEYWORD
            oferta_title = oferta.xpath('div[@class="aditem-header"]/div[@class="x4 display-desktop"]/text()').extract()
            oferta_url = oferta.xpath('div[@class="aditem-detail-container" or @class="aditem-detail-image-container"]/div[@class="aditem-detail"]/a[@class="aditem-detail-title"]/@href').extract()
            if any(word in oferta_title[0].lower() for word in KEYWORDS):
	            url = oferta_url[0]
	            yield scrapy.Request(response.urljoin(url), self.parse_oferta)

        next_page = response.xpath('//div[@class="adlist-paginator-pagelink adlist-paginator-pageselected"][last()]/a/@href').extract()

        if next_page:
            url = response.urljoin(next_page[0])
            yield scrapy.Request(url, self.parse)

    def parse_oferta(self, response):
        item = OfferItem()
        item['header'] = response.xpath('//div[@class="pagAnuCatLoc"]/text()').extract()
        item['title'] = response.xpath('//div[@class="pagAnuTituloBox"]/a/text()').extract()
        item['url'] = BASE_URL + response.xpath('//div[@class="pagAnuTituloBox"]/a/@href').extract()[0]
        item['content'] = response.xpath('//p[@class="pagAnuCuerpoAnu"]/text()').extract()
        yield item
           