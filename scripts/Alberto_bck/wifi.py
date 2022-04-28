# coding=utf-8
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
  
df = pd.read_excel("Wifi.xlsx")

sns.set_style("whitegrid")
sns.boxplot(data=df)

ax = plt.gca()
#plt.title('Gráfica diferencia entre intervalos (WIFI)',fontsize=25)
plt.xlabel("Meters",fontsize=35)
plt.xticks(rotation=45,horizontalalignment='right',fontsize=18)
plt.ylabel("Minutes",fontsize=35)
plt.yticks(np.arange(15/24/60,16/24/60 + 20/24/60/60, 10/24/60/60),fontsize=25)
a=["15:00","15:10","15:20","15:30","15:40","15:50","16:00","16:10"]
ax.set_yticklabels(a)

plt.show()