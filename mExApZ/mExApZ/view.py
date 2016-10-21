#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.encoding import smart_str

import datetime
import logging
import hashlib
import json

import mExApZ.utils.WXBizMsgCrypt

from lxml import etree


from mExApZ.utils.utils import WEIXIN_TOKEN
from mExApZ.utils.utils import ENCRYPT_KEY
from mExApZ.utils.utils import APP_ID

logger = logging.getLogger('mEmApZ')

def weixin_main(request):
	"""
	所有的消息都会先进入这个函数进行处理，函数包含两个功能，
	微信接入验证是GET方法，
	微信正常的收发消息是用POST方法。
	"""
	if request.method == "GET":
		logger.info("Get params:%s" % (request.GET))
		signature = request.GET.get("signature", None)
		timestamp = request.GET.get("timestamp", None)
		nonce = request.GET.get("nonce", None)
		echostr = request.GET.get("echostr", None)
		tmp_list = [WEIXIN_TOKEN, timestamp, nonce]
		tmp_list.sort()
		tmp_str = "%s%s%s" % tuple(tmp_list)
		tmp_str = hashlib.sha1(tmp_str).hexdigest()
		if tmp_str == signature:
			return HttpResponse(echostr)
		else:
			return HttpResponse("weixin  index")
	else:
		logger.info("POST -- GET params:%s" % (request.GET))
		logger.info("POST -- GET request.body:%s" % (request.body))
		xml_str = smart_str(request.body)
		request_xml = etree.fromstring(xml_str)
		# response_xml = auto_reply_main(request_xml)# 修改这里
		return HttpResponse(response_xml)
	pass






