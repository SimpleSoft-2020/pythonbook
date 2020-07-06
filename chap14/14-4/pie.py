import matplotlib.pyplot as plt

#饼图，按照逆时针方向排列
labels = 'Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4'
#饼图数据
sales = [30, 30, 70, 20]
explode = (0, 0, 0.0, 0.11) 
#为饼图指定颜色
colors = [(1,0,0),(0,1,0),(0,0,1),(1,1,0)]
plt.pie(sales, explode=explode, colors=colors,labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=90)
plt.show()
