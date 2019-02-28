# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_learn project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_learn'

SPIDER_MODULES = ['scrapy_learn.spiders']
NEWSPIDER_MODULE = 'scrapy_learn.spiders'

SPLASH_URL = 'http://13.56.138.124:8050'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# apperyio app 的配置
APPERYIO_DB_ID = '5c6a0be30f0d3132c406c1aa'
APPERYIO_USERNAME = 'zero'
APPERYIO_PASSWORD = 'zero'
APPERYIO_COLLECTION_NAME = 'anime'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 1
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
#     'Cookie': '''
#     first_visit_datetime_pc=2019-02-14+11%3A59%3A22; p_ab_id=6; p_ab_id_2=8; p_ab_d_id=1489096942; yuid_b=E1RTIHA; tag_view_ranking=MfZareoazp~i0UrOluTjR~BSkdEJ73Ii~X_sbgXPQ_B; c_type=28; a_type=0; b_type=1; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; is_sensei_service_user=1; login_ever=yes;
#     G_ENABLED_IDPS=google; _b="AT2ObcA1OBxGaZfeMvDc1wxh0ht9TIIX0BuJ3uJcLWGFYwts0tjbPh8mwK7g5oYMJy8="; fba=True; sessionFunnelEventLogged=1; disableUnauthGoogleOneTap=1; csrftoken=uwuZ7u0jdqucmPfN3mjuKv2AyJUD2ZaP; bei=false; cm_sub=none
#     '''
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    'scrapy_learn.middlewares.ScrapyLearnSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 添加Splash中间件，还是在settings.py中通过DOWNLOADER_MIDDLEWARES指定，并且修改HttpCompressionMiddleware的优先级
# 默认情况下，HttpProxyMiddleware的优先级是750，要把它放在Splash中间件后面
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
# 设置Splash自己的去重过滤器
# 如果你使用Splash的Http缓存，那么还要指定一个自定义的缓存后台存储介质，scrapy-splash提供了一个scrapy.contrib.httpcache.FilesystemCacheStorage的子类
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'scrapy_learn.pipelines.ScrapyLearnPipeline': 300,
# }
# 同时使用图片和文件管道
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
    # 'scrapyapperyio.ApperyIoPipeline': 300,
}
# FILES_STORE = '/path/to/valid/dir'  # 文件存储路径
IMAGES_STORE = 'images'  # 图片存储路径
# 90 days of delay for files expiration
# FILES_EXPIRES = 90
# 30 days of delay for images expiration
# IMAGES_EXPIRES = 30
# 图片缩略图
IMAGES_THUMBS = {
    'small': (120, 120),
    'big': (270, 270),
}
# 图片过滤器，最小高度和宽度
IMAGES_MIN_HEIGHT = 220
IMAGES_MIN_WIDTH = 220
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
