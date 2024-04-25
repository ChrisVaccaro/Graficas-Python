import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

df = pd.read_excel("figura5.xlsx")
df.plot(
    x = 'Month',
    kind = 'bar',
    mark_right = True)

ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.PercentFormatter())
ax.yaxis.grid(True)
ax.set_axisbelow(True)

#plt.legend(loc="lower center", bbox_to_anchor=(0.5, 0.96),fontsize=27)

plt.ylabel("MDPR",fontsize=30)
plt.yticks(fontsize=25)
#plt.ylim(0, 100)
#plt.locator_params(axis='y', nbins=10)

plt.xlabel("")
plt.xticks(rotation=0,horizontalalignment='center',fontsize=20)
#plt.title('Gráfica de interferencia por número de redes concurrentes',fontsize=25)

plt.show()
