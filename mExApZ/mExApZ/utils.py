import hashlib

token = "huihuiAiyaya"

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
