import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np






def plotBar1(y, z, x_label, y_label, modelName, x=None, title=None, font=1, ylim=0, order=None):
    if x is None:
        x = np.arange(len(y))
    data = pd.DataFrame(data={x_label: x, y_label: y, modelName: z})
    sns.set(style="white", font_scale=font)
    # tips = sns.load_dataset("tips")
    if order is not None:
	lm = sns.factorplot(x_label, y_label, hue=modelName, data=data, kind='bar', order=order)
    else:
    	lm = sns.factorplot(x_label, y_label, hue=modelName, data=data, kind='bar')
    # axes = lm.axes
    if ylim:
        lm.set(ylim=(0, ylim))
    plt.show()


#x = ['p@1', 'p@3', 'p@5', 'p@1', 'p@3', 'p@5']
#y = [64.36, 49.5, 36.04, 63.86, 50.33, 37.03]
#y = [73.27,55.28,38.61, 73.76, 56.11,38.51]
#y = [64.36, 49.5, 36.04, 63.86, 50.33, 37.03]
#z = ['MLN-SS-1O', 'MLN-SS-1O', 'MLN-SS-1O', 'MLN-SS-2O' , 'MLN-SS-2O' , 'MLN-SS-2O']
#plotBar1(y, z, 'Precision for 5% data', 'scores', 'modelNames', x=x, ylim=75, font=1.5)

x = ['5', '10', '12', '100', '1000', '5', '10', '12']
y = [9.456, 9.398, 9.23, 9.902, 12.883, 9.638, 31.663, 190.72]
z = ['MGS', 'MGS', 'MGS', 'MGS', 'MGS','ExS','ExS','ExS']
plotBar1(y, z, '# Labels', 'Times(s)', 'modelNames', x=x, ylim=200, font=1.5, order=["5",'10', '12', "100", "1000"])
