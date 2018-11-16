# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from speckle_finance.models import IEX_request

def index(request):

    iex = IEX_request(data_type="text")
    symbols = ['aapl', 'tsla']
    query_type = "book"
    full_data = iex.get_book_data(symbols, query_type)
    close_data = iex.get_close(symbols)
    close = close_data
    types = ['quote', 'news']
    batch_data = iex.get_stock_data(symbols, types)
    time_frame = "3m"
    chart_data = iex.get_chart(symbols[0], time_frame)

    context = {
        'full_data': full_data,
        'close': close,
        'batch_data': batch_data,
        'chart_data': chart_data
    }

    return render(request, 'finance/index.html', context)

def webscraper(request):

    return(HttpResponse("Testing Speckle Webscraper..."))
