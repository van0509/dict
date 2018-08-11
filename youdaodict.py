import requests,time,random,hashlib
import urllib.parse
import json


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
key=input('请输入要查询的内容')
ctime=int(time.time()*1000)
salt=str(ctime+random.randint(1,10))#1111
sign=hashlib.md5(("fanyideskweb" + key + salt + "ebSeFb%=XZ%T[KZ)c(sy!").encode('utf-8')).hexdigest()#22222

data={
    "i":key,
    "from":"AUTO",
    "to":'AUTO',
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":salt,
    "sign":sign,
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false",

}
head={
}
head['Accept'] = 'application/json, text/javascript, */*; q=0.01'
head['Accept-Encoding'] = 'gzip, deflate'
head['Accept-Language'] = 'zh-CN,zh;q=0.9'
head['Connection'] = 'keep-alive'
head['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
head[
    'Cookie'] = 'OUTFOX_SEARCH_USER_ID=-1645744815@10.169.0.84; JSESSIONID=aaa9_E-sQ3CQWaPTofjew; OUTFOX_SEARCH_USER_ID_NCOO=2007801178.0378454; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=' + str(
    ctime)
head['Host'] = 'fanyi.youdao.com'
head['Origin'] = 'http://fanyi.youdao.com'
head['Referer'] = 'http://fanyi.youdao.com/'
head[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
head['X-Requested-With'] = 'XMLHttpRequest'

da=urllib.parse.urlencode(data).encode('utf-8')

req=requests.post(url,da,headers=head).text
resp=json.loads(req)
print(resp['translateResult'][0][0]['tgt'])