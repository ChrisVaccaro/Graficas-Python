import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

df = pd.read_excel("figura10.xlsx")

df.plot(
    #x = 'Fecha y hora',
    #y = 'Building 3',
    x = 'Fecha',
    y = 'Energy Consumption',
    kind = 'line',
    marker='.',
    #figsize = (3, 2),
    mark_right = True)

ax = plt.gca()
#ax.yaxis.set_major_formatter(ticker.PercentFormatter())
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#ax.get_xaxis().set_visible(False)
#ax.set_xlim(pd.to_datetime('2018-12-25'), pd.to_datetime('2024-01-01'))

#plt.legend(loc="lower center", bbox_to_anchor=(0.5, 0.96),fontsize=27)
#plt.legend(fontsize=12)

plt.ylabel("GWh",fontsize=14)
plt.yticks(fontsize=12)
#plt.ylim(-100, 150)
#plt.locator_params(axis='y', nbins=10)

plt.xlabel("")
plt.xlim(pd.to_datetime('2018-12-25'), pd.to_datetime('2024-01-01'))
#plt.xticks(rotation=60,horizontalalignment='center',fontsize=20)
#plt.title('Gráfica de interferencia por número de redes concurrentes',fontsize=25)

plt.show()
