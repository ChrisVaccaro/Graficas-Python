import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

df = pd.read_excel("figura7.xlsx")
df.plot(
    x = 'Fecha y hora',
    y = 'Building 1',
    kind = 'line',
    mark_right = True)

ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.PercentFormatter())
ax.yaxis.grid(True)
ax.set_axisbelow(True)
ax.get_xaxis().set_visible(False)

#plt.legend(loc="lower center", bbox_to_anchor=(0.5, 0.96),fontsize=27)
plt.legend(fontsize=20)

plt.ylabel("Relative Error (%)",fontsize=30)
plt.yticks(fontsize=18)
#plt.ylim(0, 100)
#plt.locator_params(axis='y', nbins=10)

#plt.xlabel("")
#plt.xticks(rotation=60,horizontalalignment='center',fontsize=20)
#plt.title('Gráfica de interferencia por número de redes concurrentes',fontsize=25)

plt.show()
