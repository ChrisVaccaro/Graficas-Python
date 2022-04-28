# coding=utf-8
import matplotlib.pyplot as plt


grupos = ['>100h','50h-100h','15h-20h','2h-10h','1h-2h','<1h']
redes = [1,4,21,24,21,9]
grupos = ['<1h','1h - 2h','2h - 10h','15h - 20h','50h - 100h','>100h']
redes = [9,21,24,21,4,1]

grupos = ['Error E_Wh<2%','Error E_Wh>2%']
redes = [11,69]
porc = ['14%','86%']

plt.bar(grupos,redes)

for i in range(1, len(grupos)+1):
  plt.annotate(porc[i-1],(i-1,redes[i-1]+1),ha="center",fontsize=30)


plt.ylabel("Number of meters",fontsize=35)
#plt.xlabel("Periodo de medición",fontsize=20)
#plt.title('Evaluation periods',fontsize=35)
"""

plt.ylabel("Cantidad",fontsize=20)
plt.title("RESULTADOS DE COMPARACIÓN DE ENERGÍA ACTIVA",fontsize=25)
"""
plt.ylim(0,80)
plt.yticks(fontsize=25)
plt.xticks(fontsize=25)
plt.show()
