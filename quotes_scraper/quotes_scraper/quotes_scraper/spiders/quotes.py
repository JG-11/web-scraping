import scrapy

class QuotesScraper(scrapy.Spider):
    name = 'quotes' # scrapy crawl quotes

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        print('*' * 10)
        print('\n\n')
        
        title = response.xpath('//h1/a/text()').get()
        print(f'Title: {title}')
        
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        print('\nQuotes:')
        for quote in quotes:
            print(f'- {quote}')
        
        tags = response.xpath('//div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()
        print('\nTop Ten tags:')
        for tag in tags:
            print(f'- {tag}')

        print('\n\n')
        print('*' * 10)