# coding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

df = pd.read_excel("MQTT-IMPRENTA.xlsx")
fig, ax = plt.subplots(figsize = (12, 5))
plt.yticks(fontsize=25)
#ax2 = ax.twinx()

#ax.set_title('MQTT-IMPRENTA',fontsize=25)
"""
ax.plot(df['Fecha'] ,df['Active Energy (kWh) Meter'],marker='x',linewidth=4)
ax.plot(df['Fecha'] ,df['Active Energy (kWh) PQA'],marker='x',linewidth=4)
ax.set_ylim([0,16])
ax.set_ylabel('kWh',fontsize=35)
ax.yaxis.grid(color='lightgray')
ax.legend(loc='lower left', fontsize=25)

ax2.plot(df['Fecha'] ,df['Reactive Energy (kVARh) Meter'],color="green",marker='o',linewidth=4)
ax2.plot(df['Fecha'] ,df['Reactive Energy (kVARh) PQA'],color="red",marker='o',linewidth=4)
ax2.set_ylim([0,3])
ax2.set_ylabel('kVARh',fontsize=35)
ax2.legend(loc='center left', fontsize=25)
"""
ax.yaxis.grid(color='lightgray')
ax.plot(df['Fecha'] ,df['Reactive Energy (kVARh) Meter'])
ax.plot(df['Fecha'] ,df['Reactive Energy (kVARh) PQA'])
ax.set_ylim([-3,7])
ax.set_ylabel('kVARh',fontsize=35)
ax.legend(loc='upper left', fontsize=25)

ax.set_xticklabels(df['Fecha'],rotation=45,horizontalalignment='right',fontsize=20)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
#plt.yticks(fontsize=25)
#plt.tight_layout() 
plt.show()
