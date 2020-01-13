# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy_splash import SplashRequest


class DaftSpider(scrapy.Spider):
    name = 'daft'
    allowed_domains = ['daft.ie']



    def scrap_search_result_page(self, response):

    def parse(self, response):
        pass




















//paste link to start url
//override the default start_request method
//create a method to extract the links
//return a splashRequest with a 5 seco wait to allow the js to render and point to parse this