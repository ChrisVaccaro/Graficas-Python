# coding=utf-8
import matplotlib.pyplot as plt

grupos = ['Excellent', 'Good', 'Average', 'Poor', 'No coverage']
redes = [5,10,13,46,11]

plt.bar(grupos,redes,edgecolor='black')
ax=plt.gca()

for i in range(1, len(grupos)+1):
  plt.annotate(redes[i-1],(i-1,redes[i-1]+1),ha="center",fontsize=25)

#plt.grid(True,axis="y")
plt.ylabel("Number of meters",fontsize=35)
plt.ylim(0,50)
plt.yticks(fontsize=35)
#plt.xlabel("Calidad de Red",fontsize=20)
plt.xticks(fontsize=30)
#plt.title('Calidad de Red WIFI',fontsize=25)
ax.grid(axis='y')
ax.set_axisbelow(True)
plt.show()
