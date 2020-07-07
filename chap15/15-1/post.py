import urllib.parse
import urllib.request
#post数据的url
url = 'http://www.xxxx.com/submit'
#要提交的数据
values = {'name' : 'SimpleSoft',
          'addr' : 'Beijing,China',
          'age' : '28' ,
          'phone':'010-11111111'}

data = urllib.parse.urlencode(values)
#取决于服务器端要求的格式
#添加header信息,取决于服务器端是否需要
headers = {
    'Accept':'application/json, text/plain, */*',
    'Connection':'keep-alive',
    'Content-Length':'14', 
    'Content-Type':'application/x-www-form-urlencoded',
}
data = data.encode('ascii') 

req = urllib.request.Request(url, data,headers=headers)
with urllib.request.urlopen(req) as response:
   result = response.read()
