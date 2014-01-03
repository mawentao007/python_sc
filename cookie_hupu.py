import urllib2
import urllib
import re
import cookielib

url = r'http://passport.hupu.com/login?from=bbsTop'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
header = {
}
data0 = urllib.urlencode({"username":"","password":""})
req = urllib2.Request(url=url,data=data0,headers = header)
r = urllib2.urlopen(req)

header1 = {
	"Host":"bbs.hupu.com",
	"Referer":"http://bbs.hupu.com/7563592.html",
}
data1 = urllib.urlencode({
		"tid":"7563592",
		"pid":"55758",
		"state":"1",
		"authorid":"14548926",
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
text=urllib2.urlopen("http://my.hupu.com").read()
print re.search('my lover',text,re.S).group(0)

