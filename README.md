# StanfordMailingListsScrapper
Extracts all mails from stanfords mail lists


# Usage
1 - first install scrapy with the command:

pip install Scrapy

2 - clone the repository

3 - Run the following command from the project folder:

scrapy crawl Stanford -o mails.json -t json -L INFO

The mails scraped will now be at mails.json

* Note: The output will be appended to whatever file you define in the scrapy command. If it does not exist, it will create a new file.

