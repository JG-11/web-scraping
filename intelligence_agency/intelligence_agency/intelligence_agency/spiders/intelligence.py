import scrapy


class Intelligence(scrapy.Spider):
    name = 'intelligence'

    start_urls = [
        'https://www.cia.gov/library/readingroom/historical-collections'
    ]

    custom_settings = {
        'FEED_URI': 'intelligence.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse_link(self, response, **kwargs):
        link = kwargs['url']

        title = response.xpath(
            '//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath(
            '//div[@class="field-item even"]//p[not(@class)]/text()').get()

        yield {
            'url': link,
            'title': title,
            'body': paragraph
        }

    def parse(self, response):
        declassified_links = response.xpath(
            '//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()

        for link in declassified_links:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})
