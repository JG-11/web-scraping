import scrapy


class QuotesScraper(scrapy.Spider):
    name = 'quotes'  # scrapy crawl quotes

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # avoid typing explicitly the spider output storage file in the terminal
    custom_settings = {
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json'
    }

    def parse_only_quotes(self, response, **kwargs):
        kwargs['quotes'].extend(response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall())

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs=kwargs)
        else:
            yield kwargs

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall()
        tags = response.xpath(
            '//div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()

        # scrapy crawl quotes -a top=5
        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            tags = tags[:top]

        # Generator
        # scrapy crawl quotes -o quotes.json
        # scrapy crawl quotes -o quotes.csv

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]/li[@class="next"]/a/@href').get()

        # code the case where we are in the last page
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={
                'title': title,
                'quotes': quotes,
                'top_tags': tags
            })
