# coding=utf-8
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
  
df = pd.read_excel("Wifi.xlsx")
props = dict(widths=0.8,patch_artist=True, showmeans=True,
             medianprops=dict(color="black"),
             meanprops=dict(markersize="12", markerfacecolor="white", markeredgecolor="black"),
             flierprops=dict(markersize="10"))

ax = plt.gca()
box=ax.boxplot(df.values, **props)
ax.set_xticklabels(df.columns)
ax.yaxis.grid(True)
#plt.title('Gráfica diferencia entre intervalos (WIFI)',fontsize=25)
plt.xlabel("Selected Meters",fontsize=35)
plt.xticks(fontsize=25)
plt.ylabel("Time difference",fontsize=35)
#plt.yticks(np.arange(15/24/60,16/24/60 + 20/24/60/60, 10/24/60/60),fontsize=25)
#a=["15:00","15:10","15:20","15:30","15:40","15:50","16:00","16:10"]
#ax.set_ylim([14/24/60+ 58/24/60/60 ,15/24/60+ 53/24/60/60])
plt.yticks(np.arange(15/24/60,15/24/60 + 30/24/60/60, 5/24/60/60), fontsize=25)
plt.ylim(top=15/24/60 + 31/24/60/60)
a=["15'00''","15'05''","15'10''","15'15''","15'20''","15'25''","15'30''"]
ax.set_yticklabels(a)

for b in box["boxes"]:
    b.set_facecolor(next(ax._get_lines.prop_cycler)["color"])
    
plt.show()