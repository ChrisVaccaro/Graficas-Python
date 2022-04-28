# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

df = pd.read_excel("Error2.xlsx")
"""
#sns.set_style("whitegrid")
#sns.boxplot(data=df['ERROR E_Wh'])
plt.xticks(fontsize=35)

ax = plt.gca()
plt.yticks(fontsize=25)


ax.boxplot(df['ERROR E_Wh'],patch_artist=True,labels=['ERROR E_Wh'],positions=[0])
ax2 = ax.twinx()
ax2.boxplot(df['ERROR E_VARh'],patch_artist=True,labels=['ERROR E_VARh'],positions=[1])
#plt.title('Gráfica diferencia entre intervalos (Ethernet)',fontsize=25)
#plt.xlabel("Medidores",fontsize=20)

#plt.ylabel("Minutos",fontsize=20)
#plt.yticks(np.arange(0,250, 25), fontsize=25)
#a=["15:00","15:10","15:20","15:30","15:40","15:50"]
#ax.set_yticklabels(a)
ax.set_ylim([-10,245])
ax.yaxis.set_major_formatter(FormatStrFormatter('%d%%'))
ax.yaxis.grid(True)


ax2.set_ylim([-10,1005])
ax2.yaxis.set_major_formatter(FormatStrFormatter('%d%%'))

plt.show()
"""

#fig, ax1  = plt.subplots(figsize=(7.8, 5.51))
ax1 = plt.gca()
plt.xticks(fontsize=35)
plt.yticks(fontsize=25)

props = dict(widths=0.7,patch_artist=True, showmeans=True,
             medianprops=dict(color="black"),
             meanprops=dict(markersize="12", markerfacecolor="white", markeredgecolor="black"),
             flierprops=dict(markersize="10"))

box1=ax1.boxplot(df['Active Energy Error'].values, positions=[0], **props)

ax2 = ax1.twinx()
box2=ax2.boxplot(df['Reactive Energy Error'].values,positions=[1], **props)

ax1.set_xlim(-0.5,1.5)
ax1.set_xticks(range(len(df.columns)))
ax1.set_xticklabels(df.columns)
ax1.set_ylim([-10,250])
ax1.yaxis.set_major_formatter(FormatStrFormatter('%d%%'))
ax1.yaxis.grid(True)

ax2.set_ylim([-40,1000]) #ax1_ylim x4
ax2.yaxis.set_major_formatter(FormatStrFormatter('%d%%'))

for b in box1["boxes"]+box2["boxes"]:
    b.set_facecolor(next(ax1._get_lines.prop_cycler)["color"])
    
plt.yticks(fontsize=25)
plt.show()