# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from pymongo import MongoClient
from django.shortcuts import render_to_response
from django.template import RequestContext
import logging
import json
import time

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

con = MongoClient('localhost', 27017)
db = con.myblog
collection = db.users


def login(request):
	return render(request, 'login.html', {})
