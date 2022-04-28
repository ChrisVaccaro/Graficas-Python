# coding=utf-8
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
  
df = pd.read_excel("Error.xlsx")

sns.set_style("whitegrid")
sns.boxplot(data=df)

ax = plt.gca()
#plt.title('Gráfica diferencia entre intervalos (Ethernet)',fontsize=25)
#plt.xlabel("Medidores",fontsize=20)
plt.xticks(rotation=0,horizontalalignment='center',fontsize=35)
#plt.ylabel("Minutos",fontsize=20)
plt.yticks(np.arange(0,1010, 100), fontsize=25)
#a=["15:00","15:10","15:20","15:30","15:40","15:50"]
#ax.set_yticklabels(a)
ax.set_ylim([-25,1050])
ax.yaxis.set_major_formatter(FormatStrFormatter('%d%%'))
plt.show()