# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AveItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    pass

class OrderItem(scrapy.Item):
	id = scrapy.Field()
	created = scrapy.Field()
	ship_by = scrapy.Field()
	status = scrapy.Field()
	product_id = scrapy.Field()
	# not sure if redundant with product_id
	sku = scrapy.Field()
	units = scrapy.Field()
	payments = scrapy.Field()

class CustomerItem(scrapy.Item):
	name = scrapy.Field()
	# For now, don't parse address info
	address_line1 = scrapy.Field() 
	address_line2 = scrapy.Field() 
	phone = scrapy.Field()