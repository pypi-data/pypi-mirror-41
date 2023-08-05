# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['httpbin.org', 'google.com']
    # start_urls = ['http://httpbin.org/']

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'USER_AGENT': 'Mozilla/5.0',
        'COOKIES_ENABLED': False,
        'CONCURRENT_REQUESTS': 2,
        'DOWNLOAD_DELAY': 1,
        'LOGSTATS_INTERVAL': 1,
    }

    num = 1

    def start_requests(self):
        self.log(u'test Chinese: 测试中文')
        self.logger.debug('2019-01-01 00:00:01 [test] DEBUG: Resuming crawl (12345 requests scheduled)')

        self.logger.warning('warn') # python2.7 AttributeError: 'LoggerAdapter' object has no attribute 'warn'
        self.logger.error('error')
        self.logger.warning('warning\n123abc')
        self.logger.error('error\n456abc')
        self.logger.error('error\n456abc')
        self.logger.critical('critical\n789abc')
        self.logger.warning('warning\n 123\nabc')
        self.logger.error('error\n 456\nabc')
        self.logger.critical('critical')
        self.logger.critical('critical\n 789\nabc')
        self.logger.critical('critical')
        self.logger.critical('critical')

        yield scrapy.Request('http://httpbin.org/redirect/1')
        yield scrapy.Request('http://httpbin.org/status/404')
        yield scrapy.Request('http://httpbin.org/headers')
        yield scrapy.Request('http://httpbin.org/headers')
        yield scrapy.Request('https://google.com/')

    def parse(self, response):
        if self.num == 1:
            yield scrapy.Request('https://www.baidu.com/')

        yield {'item': self.num}

        self.num += 1
