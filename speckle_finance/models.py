# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime
import requests
import json

class Question (models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    #custom example method
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

#/stock/{symbol}/batch
#/stock/{symbol}/book
#/stock/{symbol}/chart/{range}
#/stock/market/collection/{collectionType}
#/stock/{symbol}/company
#/stock/market/crypto
#/stock/{symbol}/delayed-quote
#/stock/{symbol}/dividends/{range}
#/stock/{symbol}/earnings
#/stock/market/today-earnings
#/stock/{symbol}/effective-spread
#/stock/{symbol}/financials
#/stock/market/upcoming-ipos
#/stock/market/today-ipos
#/stock/{symbol}/threshold-securities
#/stock/{symbol}/short-interest
#/stock/{symbol}/stats
#/stock/{symbol}/largest-trades
#/stock/market/list
#/stock/{symbol}/logo
#/stock/{symbol}/ohlc
#/stock/{symbol}/peers
#/stock/{symbol}/previous
#/stock/{symbol}/price
#/stock/{symbol}/quote
#/stock/{symbol}/relevant
#/stock/market/sector-performance
#/stock/{symbol}/splits/{range}
#/stock/{symbol}/time-series
#/ref-data/symbols
#/ref-data/daily-list/symbol-directory
#/ref-data/daily-list/dividends
#/ref-data/daily-list/next-day-ex-date
#/tops?symbols={symbol}
#/last?symbols=
#/hist?date=
#/deep?symbols=
#/deep/book?symbols=
#/deep/trades?symbols=

class IEX_request (models.Model):

    def __init__(self):
        self.base_url = "https://api.iextrading.com/1.0"
        self.api_url = self.base_url
        self.endpoint = "/"
        self.api_key = ""
        self.data_type = "json"

    def __init__(self, data_type):
        self.base_url = "https://api.iextrading.com/1.0"
        self.api_url = self.base_url
        self.endpoint = "/"
        self.api_key = ""
        self.data_type = data_type

    def __str__(self):
        return self.api_url

    def get_base_url(self):
        return self.base_url

    def get_api_url(self):
        return self.api_url

    def set_api_url(self):
        self.api_url = self.base_url + self.endpoint

    def get_endpoint(self):
        return self.endpoint

    def get_data_type(self):
        return self.data_type

    def api_request(self):
        http_request = requests.get(self.api_url, self.api_key)
        if http_request.status_code == 200:
            if self.data_type == "text":
                api_response = http_request.text
            elif self.data_type == "json":
                api_response = json.loads(http_request.content.decode('utf-8'))
            else:
                api_response = json.loads(http_request.content.decode('utf-8'))
        else:
            api_response = "request failed"
        return api_response

    # /batch
    # /book
    # /chart/{range}
    # /company
    # /delayed-quote
    # /dividends/{range}
    # /earnings
    # /effective-spread
    # /financials
    # /threshold-securities
    # /short-interest
    # /stats
    # /largest-trades
    # /logo
    # /ohlc
    # /peers
    # /previous
    # /price
    # /quote
    # /relevant
    # /splits/{range}
    # /time-series

    def get_book_data(self, symbols, query_type):
        self.endpoint = "/stock/" + symbols[0] + "/" + query_type
        self.set_api_url()
        return self.api_request()

    def get_stock_data(self, symbols, types):
        delimiter = ""
        if len(symbols) == 1:
            self.endpoint = "/stock/" + delimiter.join(symbols) + "/batch?types="
            if len(types) > 1:
                delimiter = ","
            self.endpoint = self.endpoint + delimiter.join(types)
        else:
            delimiter = ","
            self.endpoint = "/stock/market/batch?symbols=" + delimiter.join(symbols) + "&types="
            if len(types) == 1:
                delimiter = ""
            self.endpoint = self.endpoint + delimiter.join(types)
        self.set_api_url()
        return self.api_request()

    def get_close(self, symbols):
        query_type = "book"
        self.data_type = "json"
        data = self.get_book_data(symbols, query_type)
        close = data['quote']['close']
        return str(close)

    def get_chart(self, symbol, time_frame):
        self.endpoint = "/stock/" + symbol + "/chart/" + time_frame
        self.set_api_url()
        return self.api_request()

