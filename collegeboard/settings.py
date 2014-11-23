# Scrapy settings for collegeboard project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'collegeboard'

SPIDER_MODULES = ['collegeboard.spiders']
NEWSPIDER_MODULE = 'collegeboard.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'collegeboard (+http://www.yourdomain.com)'

RETRY_TIMES=1

#DOWNLOADER_MIDDLEWARES = {
#	'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#}
