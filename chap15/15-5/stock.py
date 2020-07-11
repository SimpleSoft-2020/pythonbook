from bs4 import BeautifulSoup 
import requests
import matplotlib.pyplot as plt
#用来支持中文显示
plt.rcParams['font.sans-serif']=['SimHei','Times New Roman'] 

url='http://app.finance.ifeng.com/list/stock.php?t=ha'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
#获取所有表格行信息
table = soup.table
trs = table.find_all('tr')
stocks = []
names=[]
#打印第一行
print("股票代码 股票名称 股票最新价 涨跌幅 涨跌额 成交量 成交额 开盘价 昨天收盘价 最低价 最高价")
for tr in trs:
	#获取单元格
	tds = tr.find_all('td')
	if(len(tds) < 11):
		continue
	#对应每一个单元格数据
	p_float = float(tds[3].string.strip("%"));
	if(len(stocks) <10):
		stocks.append(p_float)
	if(len(names) < 10):
		names.append(tds[1].string)

	for td in tds:
		print(td.string,end=' ')
	#打印回车换行
	print("")

left = 1
for stock in stocks:
	plt.bar(left,stock)
	left = left+1
for xx in range(0,10):
    plt.text(xx+1, 0, names[xx], ha='center')
plt.ylabel('涨幅(%)')
plt.xlabel('个股')
plt.show()






