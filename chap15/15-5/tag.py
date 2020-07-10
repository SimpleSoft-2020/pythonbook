from bs4 import BeautifulSoup 
html = '<a href="http://example.com/book" class="bold" id="booklink">book</a>'
soup = BeautifulSoup(html)
a = soup.a
#打印tag的名字和值
print("name is ",a.name,"string is ",a.string)
#打印每个属性以及属性的值
for attr in a.attrs:
	print(attr,"=",a.attrs[attr])


