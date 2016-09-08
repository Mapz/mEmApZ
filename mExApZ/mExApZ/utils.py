import hashlib

token = "huihuiAiyaya"

def weixinValidDeveloper(timestamp , nonce , signiture):
	strList = [timestamp,token,nonce]
	strList = sorted(strList)
	strNew = ''
	for i in strList:
		strNew = strNew + i

	sha1Ret = hashlib.sha1(strNew.encode('utf-8')).hexdigest()

	print('sha1Ret:',sha1Ret)
	print('signiture:',signiture)

	return signiture == sha1Ret
