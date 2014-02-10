# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class EbayDealsItems(Item):
    category = Field()
    image = Field()
    url = Field()
    title = Field()
    price = Field()
    discount = Field()
    shipping = Field()