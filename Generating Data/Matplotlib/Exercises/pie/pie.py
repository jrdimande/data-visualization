import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D']
valores = [25, 40, 20, 15]


plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=90)

plt.title('Distribuição das Categorias')

plt.show()
