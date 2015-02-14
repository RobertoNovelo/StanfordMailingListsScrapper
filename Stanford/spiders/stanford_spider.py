# -*- coding: utf-8 -*-

"""
Spider to crawl Stanford web pages.
"""

import re
from scrapy.http import Request

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings
from Stanford.spiders.stanford_linkextractor import StanfordLinkExtractor
from Stanford.items import StanfordItem
import json


class StanfordSpider(CrawlSpider):
    """
    Define the crawler to crawl Stanford and get links
    """
    name = "Stanford"
    allowed_domains = ["stanford.edu"]
    start_urls = ['http://webcache.googleusercontent.com/search?q=cache:t9tJZTgePzUJ:https://mailman.stanford.edu/mailman/listinfo/%25E2%2580%258Bclimbing+&cd=1&hl=en&ct=clnk']

    def parse(self, response):
        rows = response.xpath('*//td/a/@href').extract()

        print "novelo"
        for row in rows:
            link = row.split("/")[-1]
            print row
            request = Request('http://mailman.stanford.edu/mailman/listinfo/' + link, callback=self.parse_link)
            yield request    

    def parse_link(self, response):
       # print response.url

        item = StanfordItem()

        mail = re.search('[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}',response.body,re.DOTALL).group(0)

        item['data'] = response.body

        item['url'] = response.url

        print item

        return item