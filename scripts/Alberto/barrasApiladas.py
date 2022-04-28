# coding=utf-8
import pandas as pd 
import matplotlib.pyplot as plt
  
df = pd.read_excel("redesWifi.xlsx")
  
df.plot( 
    x = 'Descripción', 
    kind = 'bar', 
    stacked = True,
    mark_right = True)


plt.legend(loc="lower center", bbox_to_anchor=(0.5, 0.96),fontsize=27)
plt.ylabel("Number of wifi networks",fontsize=30)
plt.yticks(fontsize=25)
plt.xlabel("Wifi Meters",fontsize=35)
plt.xticks(rotation=60,horizontalalignment='right',fontsize=20)
#plt.title('Gráfica de interferencia por número de redes concurrentes',fontsize=25)

for n in df.iloc[:, 1:]: 
  for i,(cs, ab) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n], df[n])):
    if(ab!=0):
      plt.text(i, cs - ab / 2, str(ab),  
                 va = 'center', ha = 'center',fontsize=18)

plt.show()