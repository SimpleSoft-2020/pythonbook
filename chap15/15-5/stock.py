from bs4 import BeautifulSoup 
import requests

url='http://app.finance.ifeng.com/list/stock.php?t=ha'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
#获取所有表格行信息
table = soup.table
trs = table.find_all('tr')
#打印第一行
print("股票代码 股票名称 股票最新价 涨跌幅 涨跌额 成交量 成交额 开盘价 昨天收盘价 最低价 最高价")
for tr in trs:
	#获取单元格
	tds = tr.find_all('td')
	if(len(tds) < 11):
		continue
	#对应每一个单元格数据
	for td in tds:
		print(td.string,end=' ')
	#打印回车换行
	print("")






