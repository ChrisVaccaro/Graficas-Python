# coding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FormatStrFormatter
import matplotlib.dates as mdates

df = pd.read_excel("MQTT-IMPRENTA-D.xlsx")
fig, ax = plt.subplots(figsize = (12, 5))
plt.yticks(fontsize=25)
ax2 = ax.twinx()

#ax.set_title('MQTT-IMPRENTA',fontsize=25)
ax.plot(df['Fecha'] ,df['THD [VA]'],linewidth=4)
ax.set_ylim([0,10000])
ax.yaxis.grid(color='lightgray')
ax.legend(loc='upper center', fontsize=14)

ax2.plot(df['Fecha'] ,df['Error(%)'],color="orange",linewidth=4)
ax2.set_ylim([0,250])
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f%%'))
ax2.legend(loc='upper center', fontsize=14,bbox_to_anchor=(0.5, 0.90))

ax.set_xticklabels(df['Fecha'],rotation=45,horizontalalignment='right',fontsize=20)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
plt.yticks(fontsize=25)
plt.tight_layout() 
plt.show()
