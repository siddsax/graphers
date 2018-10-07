import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def multiBarPlot(y, z, x_label, y_label, legName, x=None, title=None, font=1, ylim=0, order=None):
    if x is None:
        x = np.arange(len(y))
    data = pd.DataFrame(data={x_label: x, y_label: y, legName: z})
    sns.set(style="white", font_scale=font)
    if order is not None:
	lm = sns.factorplot(x_label, y_label, hue=legName, data=data, kind='bar', order=order)
    else:
    	lm = sns.factorplot(x_label, y_label, hue=legName, data=data, kind='bar')
    if ylim:
        lm.set(ylim=(0, ylim))
    plt.show()

x = ['5', '10', '12', '100', '1000', '5', '10', '12']
y = [9.456, 9.398, 9.23, 9.902, 12.883, 9.638, 31.663, 190.72]
z = ['MGS', 'MGS', 'MGS', 'MGS', 'MGS','ExS','ExS','ExS']
multiBarPlot(y, z, '# Labels', 'Times(s)', 'modelNames', x=x, ylim=200, font=1.5, order=["5",'10', '12', "100", "1000"])
