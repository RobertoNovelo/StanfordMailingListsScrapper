# -*- coding: utf-8 -*-

"""
Link extractors for Stanford web pages.
"""

import ast

from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.link import Link
from scrapy.utils.project import get_project_settings

class StanfordLinkExtractor(LinkExtractor):
    """
    Extract links from Stanford Listing Website
    """

    def extract_links(self, response):

        lists_page = get_project_settings().get('STANFORD_DETAILS_URL')        

        print response.url

        mails = response.xpath('*//td/a/@href').extract();


        links = [Link(lists_page % (mail.split("/")[-1]) for mail in mails)]

        print links
        
        return links