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

def all(request):
	return HttpResponse(collection.find())

def login(request):
	return render(request, 'login.html', {})
	
def do_login(request):
	account = request.POST['account']
	pwd = request.POST['pwd']	
	info = collection.find_one({"account":  account})
	if info == None or info['pwd'] != pwd:
		return HttpResponse("账号或密码不正确")
	else:
		return HttpResponse("登陆成功")
	
def register(request):
	return render(request, 'register.html', {})

lastRegTime = 0
def do_register(request):
	global lastRegTime
	account = request.POST['account']
	pwd = request.POST['pwd']	
	if pwd == "" or account == "":
		return HttpResponse("账号或密码不能为空")
		
	info = collection.find_one({"account":  account})
	if info != None:
		return HttpResponse("该账号已被注册")

	now = time.time()
	logging.debug(str(now) + " " + str(lastRegTime))
	if now - lastRegTime < 30:
		return HttpResponse("当前注册人数太多了 请稍后再试")

	lastRegTime = now
	user = {'account': account, "pwd": pwd}
	collection.insert(user)
	return HttpResponse("注册成功")
		
