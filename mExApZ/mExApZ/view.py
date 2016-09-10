#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from mExApZ.utils.utils import weixinValidDeveloper
import mExApZ.utils.WXBizMsgCrypt
import logging
from mExApZ.utils.utils import token
from mExApZ.utils.utils import encrypt_key
from mExApZ.utils.utils import app_id



# Get an instance of a logger
logger = logging.getLogger('mEmApZ')


def weixinValid(request):
	error = False
	if ('timestamp' in request.GET) and ('nonce' in request.GET):
		timestamp = request.GET['timestamp']
		nonce = request.GET['nonce']
		signature = request.GET['signature']
		echostr = request.GET['echostr']
		logger.info("timestamp:%s",timestamp)
		logger.info("nonce:%s",nonce)
		logger.info("signature:%s",signature)
		logger.info("echostr:%s",echostr)
		if (not timestamp) or (not nonce) or (not signature):
			return HttpResponse('param not right')
		else:
			valid = weixinValidDeveloper(timestamp , nonce , signature)
			if valid:
				return HttpResponse(echostr)
			else:
				return HttpResponse('not valid')

	logger.info("param not right")
	print("param not right")

	return HttpResponse('param not right')

def weixinValidSafe(request):
	error = False
	if ('timestamp' in request.GET) and ('nonce' in request.GET):
		timestamp = request.GET['timestamp']
		nonce = request.GET['nonce']
		signature = request.GET['signature']
		echostr = request.GET['echostr']
		encrypt_type = request.GET['encrypt_type']
		msg_signature = request.GET['msg_signature']
		logger.info("request.GET:%s",request.GET)
		if (not timestamp) or (not nonce) or (not signature):
			return HttpResponse('param not right')
		elif encrypt_type == "aes":
			decrypt_test = WXBizMsgCrypt(token,encrypt_key,app_id)
			ret ,decryp_xml = decrypt_test.DecryptMsg(from_xml, msg_signature, timestamp, nonce)
			print(ret,decryp_xml)
			logger.info("ret:%s\ndecryp_xml:%s" % (ret,decryp_xml))
			if ret == 0 :
				return HttpResponse(echostr)
			else:
				return HttpResponse('not valid') 
		else:
			valid = weixinValidDeveloper(timestamp , nonce , signature)
			if valid:
				return HttpResponse(echostr)
			else:
				return HttpResponse('not valid')

	logger.info("param not right")
	print("param not right")

	return HttpResponse('param not right')



