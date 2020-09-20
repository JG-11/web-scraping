import scrapy


class QuotesScraper(scrapy.Spider):
    name = 'quotes'  # scrapy crawl quotes

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # avoid typing explicitly the spider output storage file in the terminal
    custom_settings = {
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    """
        Other custom settings options:
        1. CONCURRENT_REQUESTS
        2. MEMUSAGE_LIMIT_MB
        3. MEMUSAGE_NOTIFY_MAIL
        4. ROBOTSTXT_OBEY
        5. USER_AGENT
    """

    def get_quotes_and_authors(self, response):
        quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall()
        authors = response.xpath(
            '//div[@class="quote"]/span[not(@class)]/small/text()').getall()

        quotes_authors = [{'text': text, 'author': author}
                          for text, author in zip(quotes, authors)]

        return quotes_authors

    def parse_only_quotes(self, response, **kwargs):
        kwargs['quotes'].extend(self.get_quotes_and_authors(response))

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs=kwargs)
        else:
            yield kwargs

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        quotes = self.get_quotes_and_authors(response)
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
