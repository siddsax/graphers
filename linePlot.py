import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def linePlot(y, x_label, y_label, x=None, z=None, z_label=None, title=None, font=1):
    if x is None:
        x = np.arange(len(y))


    sns.set(style="white", font_scale=font)

    
    if z_label is not None:
        df = pd.DataFrame({x_label : x, z_label: z, y_label : y})
        sns.tsplot(df, time=x_label, unit = z_label, condition=z_label, value=y_label)
    else:
        df = pd.DataFrame({x_label : x, y_label : y})
        sns.lineplot(x= x_label, y = y_label, data=df)

    if title is not None:    
        plt.title(title)

    plt.show()



x = np.array(range(10))+1
y = np.array([90.800, 92.330, 93.180, 93.760, 94.140, 94.130, 94.270, 94.220, 94.210, 94.170 ])

x_label = 'Models'
y_label = 'Accuracies'
title = 'Accuracies on Cifar10'

# x = np.array([5, 10, 20, 30, 5, 10, 20, 30])#.reshape((2, 4))
# y1 =  [28.37, 30.97, 33.03, 33.27]
# y2 =  [30.14, 33.21, 36.06, 38.06]
# y = np.array(y1 + y2)
# z = ['label-1']*len(y1) + ['label-2']*len(y2)
# z_label = 'Model'


linePlot(y, x_label, y_label, x, title=title)


