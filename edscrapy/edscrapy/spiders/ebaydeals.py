from urlparse import urljoin

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from edscrapy.utils import iextract, istrip
from edscrapy.items import EbayDealsItems

class EbayDeals(Spider):
    name = 'ebaydeals'
    start_urls = ["http://globaldeals.ebay.com/"]

    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath('//div[@id="scrollable"]/ul/li/a/@href').extract()
        for link in links:
            url = urljoin(response.url, link)
            return Request(url, callback=self.products)

    def products(self, response):
        sel = Selector(response)
        heading = istrip("".join(sel.xpath('//div[@class="checkForLarge pnlItems l2"]/h2/text()').extract()))
        cards = sel.xpath('//div[@class="checkForLarge pnlItems l2"]/div[@class="wrapper"]/div[contains(@class, "card")]')
        for i, card in enumerate(cards):
            item = EbayDealsItems()
            item["heading"] = heading
            if card.xpath('div[@class="first"]/div[@class="imgBox"]/img[@class="gallery-image"]/@data-src'):
                img = card.xpath('div[@class="first"]/div[@class="imgBox"]/img[@class="gallery-image"]/@data-src').extract()
            else:
                img = card.xpath('div[@class="first"]/div[@class="imgBox"]/img[@class="gallery-image"]/@src').extract()
            item["img"] = iextract(img)
            item["link"] = iextract(card.xpath('div[@class="second"]/a[@class="description"]/@href').extract())
            item["title"] = iextract(card.xpath('div[@class="second"]/a[@class="description"]/span/text()').extract())
            item["price"] = iextract(card.xpath('div[@class="second"]/span[@class="price"]/text()').extract())
            item["discount"] = iextract(card.xpath('div[@class="second"]/span[@class="discount"]/text()').extract())
            item["shipping"] = iextract(card.xpath('div[@class="second"]/span[@class="free-postage"]/text()').extract())
            yield item