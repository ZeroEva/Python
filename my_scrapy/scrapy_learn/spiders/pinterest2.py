#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import base64
import json
import re

import scrapy
from scrapy_splash import SplashRequest


class StackOverflowSpider(scrapy.Spider):
    name = 'pinterest2'
    allowed_domains = ["pinterest.com"]
    start_urls = ['https://www.pinterest.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Cookie': 'G_ENABLED_IDPS=google; _b="AT2ObcA1OBxGaZfeMvDc1wxh0ht9TIIX0BuJ3uJcLWGFYwts0tjbPh8mwK7g5oYMJy8="; fba=True; _routing_id="a93f073c-1f0d-4465-871a-9b8d8595a2a2"; bei=false; logged_out=True; sessionFunnelEventLogged=1; G_AUTHUSER_H=0; _auth=1; csrftoken=FfK4Ca3PDPEXlzk60suMdzWe2P5OE3ZO; _pinterest_sess="TWc9PSZSa2FIelVnQ1JuWjY5TWhuVWtqQjBSSWs0dVhwSjNCYzA4TU5NYmRTZG40ZStFc1NkNmo5M3loR1JmNmtDc25yTGprZEp3MHE0eUhHZ3plU29iUzRXYzdTUHpkNUE0OHB1U3dueUUzYVE4SnIwRHN2ZUJXM2cvRG1ndzRCRUw4V055M1luZGlKS3JpcVd5bTJmeWQrOTdPQ2ZUNHlrT2F2UkRmaXNFWEZBa3RiNEtIYUNJTDlFYkNwRHZ3N0VFZzFGWWc0bm9uOE5QUFpOdVFybjI1SUJDR2xCRVFzS2VJQkdKaEV4clByQW9Lc1RWclJMTW5vZ21oRUFFQis2RVJZM3F6R1JsVjFHZXdBcGNBWDU3bjIxckZlU28xdnB1QmJEdk8yNmQyS2g2UEVBalYrSlc5cjJUSGtzL1BsK2Ivc3NtV3d1ZHNYMFR4ZmJ3YXlFQ3QxMUFMVThFRUEvTk9FUldzdEhTODVSUEV3L2FvNlYzeTRqUnlJNERGeHhmRVl4Q2tXZXZhQTY5eDRGOGRBN3NjaEh5Y1ZXZEMzSWdyb2VoZDBSNEF1d0hxYmc5ZGQ5dHNLZXd3aUFSWHduRVhOSitlY0NsMnRTUTR3dlprKzRYWjZ2by9TN1F6RTY1bnRxSHJsUENjMllPNm55TDF3cGVkLzc5NE5QblNMYk9kTFYyVDBYcjVFN0laTnNka09ybzR3TlZWanZocjEwb0I5TW43Uk9mOUsvcnprL3YzTUdLZVhiVEZJNVRRZ0QzTXBiS01oNEloVXZ6aDhxa2ZhMnFkREdJcHZXYlBreVhGV2NTNUZPUU9QNE1MQmlicUUzOU9XU1FrTkozK2Q3WmJOZUh2Zy8rNGpsbVltQW1WVzRrZXNRYkJYV2lDd2pqQlEwYkxFSXd1UVVzNDNwdGs2bk1rQS9JUURrb0lzRTdvVzZBMVc5Mjh0aERZaXkwTllkMWJjcDFTeExDY1NkQmJ1ZmV0UG1KMGdYb0FwVVcwYnR5QXRJanBMcmVpV2NLbWNDeFJpdDhkdzI2b29SOUpPbG5FUzlxUWlpQTJRbDN6NHZIclM2UjdJM0VVM21EMEh1T2FyUXZLZE5QQ0huelF2YnlXNVB3QlFSQkV0TG1XWHJxNzNhWGhIamRhZTBXbTE3UGdQdzFvSVkwcllmMWV0cTRXblhCMkZZSXhhbGhVR3IwSEVHMko2WUZScDlKMzFxVGg2YUJiZ2tUaXBLeGZhVVBKMHEwcjAvb3M9JjlQY0cvSHd2ZS9uQzVLNVZxQmY5eURGRGN1cz0="; cm_sub=none',
    }
    cookies = {
        'sessionFunnelEventLogged': '1',
        '_auth': '1',
        'logged_out': 'True',
        'G_AUTHUSER_H': '0',
        '_pinterest_sess': '"TWc9PSZSa2FIelVnQ1JuWjY5TWhuVWtqQjBSSWs0dVhwSjNCYzA4TU5NYmRTZG40ZStFc1NkNmo5M3loR1JmNmtDc25yTGprZEp3MHE0eUhHZ3plU29iUzRXYzdTUHpkNUE0OHB1U3dueUUzYVE4SnIwRHN2ZUJXM2cvRG1ndzRCRUw4V055M1luZGlKS3JpcVd5bTJmeWQrOTdPQ2ZUNHlrT2F2UkRmaXNFWEZBa3RiNEtIYUNJTDlFYkNwRHZ3N0VFZzFGWWc0bm9uOE5QUFpOdVFybjI1SUJDR2xCRVFzS2VJQkdKaEV4clByQW9Lc1RWclJMTW5vZ21oRUFFQis2RVJZM3F6R1JsVjFHZXdBcGNBWDU3bjIxckZlU28xdnB1QmJEdk8yNmQyS2g2UEVBalYrSlc5cjJUSGtzL1BsK2Ivc3NtV3d1ZHNYMFR4ZmJ3YXlFQ3QxMUFMVThFRUEvTk9FUldzdEhTODVSUEV3L2FvNlYzeTRqUnlJNERGeHhmRVl4Q2tXZXZhQTY5eDRGOGRBN3NjaEh5Y1ZXZEMzSWdyb2VoZDBSNEF1d0hxYmc5ZGQ5dHNLZXd3aUFSWHduRVhOSitlY0NsMnRTUTR3dlprKzRYWjZ2by9TN1F6RTY1bnRxSHJsUENjMllPNm55TDF3cGVkLzc5NE5QblNMYk9kTFYyVDBYcjVFN0laTnNka09ybzR3TlZWanZocjEwb0I5TW43Uk9mOUsvcnprL3YzTUdLZVhiVEZJNVRRZ0QzTXBiS01oNEloVXZ6aDhxa2ZhMnFkREdJcHZXYlBreVhGV2NTNUZPUU9QNE1MQmlicUUzOU9XU1FrTkozK2Q3WmJOZUh2Zy8rNGpsbVltQW1WVzRrZXNRYkJYV2lDd2pqQlEwYkxFSXd1UVVzNDNwdGs2bk1rQS9JUURrb0lzRTdvVzZBMVc5Mjh0aERZaXkwTllkMWJjcDFTeExDY1NkQmJ1ZmV0UG1KMGdYb0FwVVcwYnR5QXRJanBMcmVpV2NLbWNDeFJpdDhkdzI2b29SOUpPbG5FUzlxUWlpQTJRbDN6NHZIclM2UjdJM0VVM21EMEh1T2FyUXZLZE5QQ0huelF2YnlXNVB3QlFSQkV0TG1XWHJxNzNhWGhIamRhZTBXbTE3UGdQdzFvSVkwcllmMWV0cTRXblhCMkZZSXhhbGhVR3IwSEVHMko2WUZScDlKMzFxVGg2YUJiZ2tUaXBLeGZhVVBKMHEwcjAvb3M9JjlQY0cvSHd2ZS9uQzVLNVZxQmY5eURGRGN1cz0="',
        '_routing_id': '"a93f073c-1f0d-4465-871a-9b8d8595a2a2"',
        'G_ENABLED_IDPS': 'google',
        '_b': '"AT2ObcA1OBxGaZfeMvDc1wxh0ht9TIIX0BuJ3uJcLWGFYwts0tjbPh8mwK7g5oYMJy8',
        'csrftoken': 'FfK4Ca3PDPEXlzk60suMdzWe2P5OE3ZO',
        'fba': 'True',
        'bei': 'false',
    }
    proxies = 'http://127.0.0.1:60000'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, cookies=self.cookies, meta={'proxy': self.proxies})

    def parse(self, response):
        # print("=====", response.data['header'])
        # print("=====", response.data)
        # image_list = response.css('.Masonry').extract()
        # print(image_list)
        # # print("=====", response.body)
        # print("======", response.css('.Masonry').extract())
        xpath = response.css(".AppBase .appContent .gridCentered .Masonry .Collection-Item a::attr(href)").getall()
        # print("======", xpath)
        for url in xpath:
            if url.startswith('/pin'):
                yield scrapy.Request(response.urljoin(url), callback=self.picture_parse, headers=self.headers,
                                     cookies=self.cookies, meta={'proxy': self.proxies})
        # with open('body.json', 'w') as f:
        #     f.write(response.body.decode('UTF-8'))
        # with open('jt.png', 'wb') as f:
        #     f.write(base64.b64decode(response.data['png']))
        # with open('a.html', 'wb') as f:
        #     f.write(response.body)
        #
        # with open("body.html", 'w') as f:
        #     findall = re.findall('<body>.*</body>', response.body.decode('UTF-8'))
        #     for every in findall:
        #         f.write(every)

    def picture_parse(self, response):
        src = response.css(".imageLink::attr(href)").get()
        search = re.search(r'(jp[e]?g)|(png)', src)
        if search:
            with open('a.html', 'a') as f:
                f.write(f'<img src="{src}" />\n')

        pass

    def error_parse(self, response):
        print("======", "error")
