from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from mExApZ.utils import weixinValidDeveloper

def weixinValid(request):
	error = False
	if ('timestamp' in request.GET) and ('nonce' in request.GET):
		timestamp = request.GET['timestamp']
		nonce = request.GET['nonce']
		signiture = request.GET['signiture']
		echostr = request.GET['echostr']
		if (not timestamp) or (not nonce) or (not signiture):
			error = True
		else:
			valid = weixinValidDeveloper(timestamp , nonce , signiture)
			if valid:
				return HttpResponse(echostr)
			else:
				return HttpResponse('not valid')

	print("param not right")


