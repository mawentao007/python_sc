import urllib2
import urllib
import re
import cookielib

url = r'http://passport.hupu.com/login?from=bbsTop'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
header = {
	"User-Agent":r"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0"
}
data0 = urllib.urlencode({"username":"_Mourinho_","password":"111111mmm"})
req = urllib2.Request(url=url,data=data0,headers = header)
r = urllib2.urlopen(req)

header1 = {
	"(Request-Line)":r"POST /ajax/lights.ajax.php HTTP/1.1",
	"Host":"bbs.hupu.com",
	"Accept":r"*/*",
#	"Accept-Language":"en-US,en;q=0.5",
#	"Accept-Encoding":"gzip,deflate",
#	"Content-type":"application/x-www-form-urlencoded;charset=UTF-8",
#	"X-Requested-With":"XMLHttpRequest",
	"Referer":"http://bbs.hupu.com/7563592.html",
#	"User-Agent":r"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
#	"Connection":"keep-alive",
#	"Content-Lenght":"55",
#	"Pragma":"no-cache",
#	"Cache-Control":"no-cache"
}
data1 = urllib.urlencode({
		"tid":"7563592",
		"pid":"66895",
		"state":"1",
		"authorid":"15662824",
		"fid":"138"
		})
url1 = "http://bbs.hupu.com/ajax/lights.ajax.php"
req1 = urllib2.Request(
		url = url1,
		data = data1,
		headers = header1
		)
try:
	ans = urllib2.urlopen(req1)
	print ans.getcode()
except urllib2.HTTPError,e:
	print e.code
#text=urllib2.urlopen("http://my.hupu.com").read()
#print re.search('my lover',text,re.S).group(0)

