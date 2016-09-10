#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
import hashlib

token = "huihuiAiyaya"
encrypt_key = "hW1KgvdaAYyP3ATPM1TQU9kzXtVeApya8AnXanS5TEe"
app_id = "wxd3de8e894c7be16a"

def weixinValidDeveloper(timestamp , nonce , signature):
	strList = [timestamp,token,nonce]
	strList = sorted(strList)
	strNew = ''
	for i in strList:
		strNew = strNew + i

	sha1Ret = hashlib.sha1(strNew.encode('utf-8')).hexdigest()

	print('sha1Ret:',sha1Ret)
	print('signature:',signature)

	return signature == sha1Ret
