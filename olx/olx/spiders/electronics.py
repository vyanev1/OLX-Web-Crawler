import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import OlxItem
from transliterate import translit
import re


def has_cyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))


def format_text(text):
    if has_cyrillic(text):
        return translit(text, 'bg', reversed=True)
    return text


class ElectronicsSpider(CrawlSpider):
    name = 'electronics'
    allowed_domains = ['www.olx.bg']
    start_urls = ['https://www.olx.bg/elektronika/telefoni/']
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_itemlist",
             follow=True),)

    def parse_itemlist(self, response):
        print('Processing..' + response.url)
        item_links = response.css('h3 > .detailsLink::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        print('Details page..' + response.url)
        item = OlxItem()
        item['title'] = format_text(response.css('h1::text').extract()[0].strip())
        item['price'] = float(response.css('.pricelabel > strong::text').extract()[0][:-3])
        item['location'] = format_text(response.css('.offer-user__address > address > p::text').extract()[0])
        item['condition'] = format_text(response.css('.offer-details__value::text').extract()[-1])
        item['url'] = response.url
        yield item

    def parse(self, response):
        pass
