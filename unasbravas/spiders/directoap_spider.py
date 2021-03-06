import scrapy

from unasbravas.items import RecipeItem

KEYWORDS = ['patata', 'brava']

class DirectoAPSpider(scrapy.Spider):
    name = 'directoap'
    start_urls = ['http://www.directoalpaladar.com']

    def parse(self, response):
        for recipe in response.xpath('//h2[@class="article-home-header"]/a'):
            recipe_title = recipe.xpath('text()').extract()
            # If title contains any KEYWORD
            if any(word in recipe_title[0].lower() for word in KEYWORDS):
                url = recipe.xpath('@href').extract()
                yield scrapy.Request(response.urljoin(url[0]), self.parse_recipe)

        next_page = response.css('a.btn-next::attr(href)')

        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

    def parse_recipe(self, response):
        item = RecipeItem()
        item['title'] = response.xpath('/div[@class="article-header"]/header/h1/span/text()').extract()
        item['link'] = response.url
        yield item
