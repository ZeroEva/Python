#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import base64
import json
import re

import scrapy
from scrapy_splash import SplashRequest


class StackOverflowSpider(scrapy.Spider):
    name = 'pinterest'
    allowed_domains = ["pinterest.com"]
    start_urls = ['https://www.pinterest.com']
    username = "hao.sunshine.eva@gmail.com"
    password = "hao0822.."
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    cookies = [
        {
            'name': 'G_ENABLED_IDPS',
            'value': 'google'
        },
        {
            'name': '_auth',
            'value': '1'
        },
        {
            'name': '_b',
            'value': '"AT2ObcA1OBxGaZfeMvDc1wxh0ht9TIIX0BuJ3uJcLWGFYwts0tjbPh8mwK7g5oYMJy8="'
        },
        {
            'name': '_routing_id',
            'value': 'a93f073c-1f0d-4465-871a-9b8d8595a2a2'
        },
        {
            'name': '_pinterest_sess',
            'value': '"TWc9PSZacmI0cmpyUE5ybEZpdEJNR0tZeGx1dE82Q0JMOFBVajdoZDMvVVlwdGl3aithcVg4eGRJZHA2RnM0T0JWLzR1eUo1U2I0MlgxVEpZclhlUFJ5Z0Rod0Z0c08xaXd5OHpDbkV2WHE0YVd1NmVkSnNmWlE3blVreWFBaXdMaE5LMmRuVVpXVG5VdXBSMnVRREZWUUpqK3gzWnlEbVVVVHhwcndsa05vNWRzeENNNit6K1RRMnFHUExQSzJYaUFqdHdFU0hJZ00rR1VSNlRaMmpnT3pkZnBJOS8yNnFkblJCRzg1KzFWQzdrNTVlYThJYi8rbmpSRHdNTUhhUXAxYW02cU80QituK2R4UG01d0tUaDUvUlZ0MjhuVzYwQ3hDc1l6RmlvdVJheGRCOUNYWFBpckZjU2tKK0xXTzQzeVZkb29DM2l3VHZCTndzcmxhQ1BhVjhQWTE3WFg2N05UelNEUlhXakJ6aWNCMXRxM0hMeklXNEZOVjYwN1h1UmlBMUJJSkhiTkVJcCtab0RwMjVZeE1hS1hqWU5nWjVLUmJLOVluQmNnd2cxVjJzd1pFbmRJb3R3NWVEWUZtdGVWakhIakRMYjhGa2tOT0k3enI0L0JIKyswZ0NsdUMzNUJGaXd3Z00vbmw1LzdhTG1xWlNUSTB6a3MvQ2QwY1NSUzVOVFNVREJXd2lyMlluWnlZYXJudmlkUzFvMENaWTRRd01ERW1tcVUzSjlCRmczdEVZcmdpZFJpbjRPWmc2dzR5dnZkejVrdWd3bllDWFU1LzhMaVkzUXNMeHBRcnIwSmZVcXZXb1N1ZXJCc1p5S3JtbWxJa21pMjBTK1NxSGxuQ0o0b1NrcGwrNFJjT0JMZjRYRHdmVUFxTWR0SWdqZk52b1hnWXg2VnR1aENYN2FVWURxZisvcW1YdFNVdU1PQlduUE83SWxVc3VzeEpGZ1MzOGF6QzJQdWxIRG85eXlheEM2QnJ1MGZBZVYxTlo2WkczSWNQSXE3dW5qNHl1eEttaW5GSjZDZzl4VnpWdzQ4VEpkNU5YUUc1TFJCUFYyNmJDYmtFV2JscjV2SGRRTGtVV00xbVRvcGFIRkhMQk9UZ2szclNCUVdxaTFaWkNlamZYMG1nZ0xKcUtNQnNDZWN0bll2MmhHZXdiNHpPcFhiTDBya0l0dHNCRytLeVV1L3pUK2d0akxhczlZV1NoS0tCUURSNjZwb05ScVFKWGRBUGM0WEg5SXhzM1JaYnc9JjZXOTJFdTA1U2gzTWRqa3U5S3RCL3MrWThCUT0="'
        },
        {
            'name': 'bei',
            'value': 'false'
        },
        {
            'name': 'cm_sub',
            'value': 'none'
        },
        {
            'name': 'csrftoken',
            'value': 'uwuZ7u0jdqucmPfN3mjuKv2AyJUD2ZaP'
        },
        {
            'name': 'fba',
            'value': 'True'
        },
        {
            'name': 'sessionFunnelEventLogged',
            'value': '1'
        },
        {
            'name': '_pinterest_referrer',
            'value': '9597446c-8fb3-4e0d-ab0e-3ea0459dbc62'
        },
    ]
    lua_headers = '''{
        ['Cookie'] = 'G_ENABLED_IDPS=google; _b="AT2ObcA1OBxGaZfeMvDc1wxh0ht9TIIX0BuJ3uJcLWGFYwts0tjbPh8mwK7g5oYMJy8="; fba=True; disableUnauthGoogleOneTap=1; _auth=1; csrftoken=uwuZ7u0jdqucmPfN3mjuKv2AyJUD2ZaP; _pinterest_sess="TWc9PSZacmI0cmpyUE5ybEZpdEJNR0tZeGx1dE82Q0JMOFBVajdoZDMvVVlwdGl3aithcVg4eGRJZHA2RnM0T0JWLzR1eUo1U2I0MlgxVEpZclhlUFJ5Z0Rod0Z0c08xaXd5OHpDbkV2WHE0YVd1NmVkSnNmWlE3blVreWFBaXdMaE5LMmRuVVpXVG5VdXBSMnVRREZWUUpqK3gzWnlEbVVVVHhwcndsa05vNWRzeENNNit6K1RRMnFHUExQSzJYaUFqdHdFU0hJZ00rR1VSNlRaMmpnT3pkZnBJOS8yNnFkblJCRzg1KzFWQzdrNTVlYThJYi8rbmpSRHdNTUhhUXAxYW02cU80QituK2R4UG01d0tUaDUvUlZ0MjhuVzYwQ3hDc1l6RmlvdVJheGRCOUNYWFBpckZjU2tKK0xXTzQzeVZkb29DM2l3VHZCTndzcmxhQ1BhVjhQWTE3WFg2N05UelNEUlhXakJ6aWNCMXRxM0hMeklXNEZOVjYwN1h1UmlBMUJJSkhiTkVJcCtab0RwMjVZeE1hS1hqWU5nWjVLUmJLOVluQmNnd2cxVjJzd1pFbmRJb3R3NWVEWUZtdGVWakhIakRMYjhGa2tOT0k3enI0L0JIKyswZ0NsdUMzNUJGaXd3Z00vbmw1LzdhTG1xWlNUSTB6a3MvQ2QwY1NSUzVOVFNVREJXd2lyMlluWnlZYXJudmlkUzFvMENaWTRRd01ERW1tcVUzSjlCRmczdEVZcmdpZFJpbjRPWmc2dzR5dnZkejVrdWd3bllDWFU1LzhMaVkzUXNMeHBRcnIwSmZVcXZXb1N1ZXJCc1p5S3JtbWxJa21pMjBTK1NxSGxuQ0o0b1NrcGwrNFJjT0JMZjRYRHdmVUFxTWR0SWdqZk52b1hnWXg2VnR1aENYN2FVWURxZisvcW1YdFNVdU1PQlduUE83SWxVc3VzeEpGZ1MzOGF6QzJQdWxIRG85eXlheEM2QnJ1MGZBZVYxTlo2WkczSWNQSXE3dW5qNHl1eEttaW5GSjZDZzl4VnpWdzQ4VEpkNU5YUUc1TFJCUFYyNmJDYmtFV2JscjV2SGRRTGtVV00xbVRvcGFIRkhMQk9UZ2szclNCUVdxaTFaWkNlamZYMG1nZ0xKcUtNQnNDZWN0bll2MmhHZXdiNHpPcFhiTDBya0l0dHNCRytLeVV1L3pUK2d0akxhczlZV1NoS0tCUURSNjZwb05ScVFKWGRBUGM0WEg5SXhzM1JaYnc9JjZXOTJFdTA1U2gzTWRqa3U5S3RCL3MrWThCUT0="; bei=false; cm_sub=none; _routing_id="9597446c-8fb3-4e0d-ab0e-3ea0459dbc62"; sessionFunnelEventLogged=1; _pinterest_referrer="https://www.google.com/",
    }'''
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # my_data = splash:evaljs("document.getElementsByClassName('Masonry')[0].innerHTML"),
    lua_source = '''
        function main(splash, args)
            splash:init_cookies(args.cookies)
            splash:set_user_agent(args.ua)
            splash:wait(5)
            splash:go(args.url)
            local element = splash:select('.GoogleConnectButton')
            local bounds = element:bounds()
            assert(element:mouse_click{x=bounds.width/3, y=bounds.height/3})
            return {
                cookies = splash:get_cookies(),
                png = splash:png(),
                ua = splash:evaljs("navigator.userAgent"),
                my_data = splash:evaljs("document.getElementsByClassName('Masonry')[0].innerHTML"),
            }
        end
    '''
    js_source = '''
    function main(){
    text1 = "success1"
    console.log(text1)
    return {
            text2 = "success2",
            text3 = "success3"
        }}
    '''

    def start_requests(self):
        splash_args = {
            'script': 1,
            'png': 1,
            'wait': 0.5,
            'js_source': self.js_source,
            'lua_source': self.lua_source,
            'ua': self.ua,
            'cookies': self.cookies,
        }
        for url in self.start_urls:
            yield SplashRequest(url,
                                self.parse,
                                endpoint='execute',
                                args=splash_args,
                                errback=self.error_parse,
                                headers=self.headers)

    def parse(self, response):
        # print("=====", response.data['header'])
        # print("=====", response.data)
        # image_list = response.css('.Masonry').extract()
        # print(image_list)
        # # print("=====", response.body)
        print("======", response.data['my_data'])

        # with open('body.json', 'w') as f:
        #     f.write(response.body.decode('UTF-8'))
        with open('jt.png', 'wb') as f:
            f.write(base64.b64decode(response.data['png']))
        # with open('data.json', 'w') as f:
        #     f.write(response.data)
        #
        # with open("body.html", 'w') as f:
        #     findall = re.findall('<body>.*</body>', response.body.decode('UTF-8'))
        #     for every in findall:
        #         f.write(every)

    def error_parse(self, response):
        print("======", "error")
