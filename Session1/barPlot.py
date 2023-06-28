import matplotlib.pyplot as plt

products = ['Product 1','Product 2','Product 3','Product 4']
sales=[350,400,290,520]

plt.bar(products,sales,color=['red', 'blue', 'green', 'orange'])
plt.xlabel('Product 1')
plt.ylabel('Sales')
plt.title('Sales Date')
plt.legend(['Ipone','Samsung','Macbook','iMac'])
plt.show()
