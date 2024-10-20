# Scrapy settings for phones project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'phones'

SPIDER_MODULES = ['phones.spiders']
NEWSPIDER_MODULE = 'phones.spiders'
FEEDS = {
    #'test.json': { 'format': 'json'},
    'data.json': { 'format': 'json'},
    'data.csv': { 'format': 'csv'},
 }
FEED_EXPORT_FIELDS = ['phone_brand','phone_model','price','specs','pricing']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'phones (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'phones.middlewares.PhonesSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'phones.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 300,
    #'phones.middlewares.CustomRedirectMiddleware': 600,
    #'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 700,
    'phones.middlewares.ScrapeOpsFakeUserAgentMiddleware' : 500,
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    #'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    #'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}
SCRAPEOPS_API_KEY = ''
SCRAPE_FAKE_USER_AGENT_ENABLED = False
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPE_NUM_RESULTS = 100
SCRAPEOPS_PROXY_ENABLED = False
REDIRECT_ENABLED = False
CONCURRENT_REQUESTS=5
DOWNLOAD_DELAY=0
DOWNLOAD_TIMEOUT = 120
#HTTPERROR_ALLOWED_CODES = [302]
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'phones.pipelines.PhonesPipeline': 300,
    #'phones.pipelines.CsvExportPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#ROTATING_PROXY_LIST = [
#    
#    '34.230.34.121:4920',
#    
#]
#ROTATING_PROXY_LIST_PATH = 'proxies.txt'
