# -*- coding: utf-8 -*-

# Scrapy settings for Stanford project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Stanford'

SPIDER_MODULES = ['Stanford.spiders']
NEWSPIDER_MODULE = 'Stanford.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Roberto Novelo'

# Stanford settings
STANFORD_DETAILS_URL = 'http://mailman.stanford.edu/mailman/listinfo/%s'
STANFORD_LIST_URL = 'http://mailman.stanford.edu/mailman/listinfo/climbing'
          

CONCURRENT_ITEMS = 200
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 16
ROBOTSTXT_OBEY = True
COOKIES_ENABLED = False
LOG_ENABLED = False

LOG_FILE = 'application.log'