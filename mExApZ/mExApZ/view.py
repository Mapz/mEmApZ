from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from mExApZ.utils import weixinValidDeveloper
import logging

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
			error = True
		else:
			valid = weixinValidDeveloper(timestamp , nonce , signature)
			if valid:
				return HttpResponse(echostr)
			else:
				return HttpResponse('not valid')

	logger.info("param not right")
	print("param not right")

	return HttpResponse('param not right')


