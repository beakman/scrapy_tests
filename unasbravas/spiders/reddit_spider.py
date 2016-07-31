import scrapy

from unasbravas.items import RecipeItem

KEYWORDS = ['patata', 'brava']

class RedditRecipesSpider(scrapy.Spider):
    name = 'redditrecipes'
    
    start_urls = []
    
    for keyword in KEYWORDS:
        start_urls.append('https://www.reddit.com/r/recipes/search?q=' + keyword + '&restrict_sr=on')

    def parse(self, response):
        for recipe in response.xpath('//header[@class="search-result-header"]/a'):
            recipe_title = recipe.xpath('text()').extract()
            # If title contains any KEYWORD
            if any(word in recipe_title[0].lower() for word in KEYWORDS):
                url = recipe.xpath('@href').extract()
                yield scrapy.Request(response.urljoin(url[0]), self.parse_recipe)

        next_page = response.xpath('//a[@rel="nofollow next"]/@href')

        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

    def parse_recipe(self, response):
        item = RecipeItem()
        item['title'] = response.css("p.title > a.title::text").extract()
        item['link'] = response.url
        yield item
