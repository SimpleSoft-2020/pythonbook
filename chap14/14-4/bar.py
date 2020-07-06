import matplotlib.pyplot as plt
#绘制柱状图
#用来支持中文显示
plt.rcParams['font.sans-serif']=['SimHei','Times New Roman'] 
 
sales = [30, 30, 70, 20,80,30,45,80,20,30,12,13]
left = 1
for sale in sales:
	plt.bar(left,sale)
	left = left+1
plt.ylabel('增长额')
plt.title('销售增长额')
plt.xlabel('月份')
plt.show()
