import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib
import pandas as pd

def barPlot(y, x_label, y_label, x=None, title=None, font=1, ylim=0, extreme=0):
    if x is None:
        x = np.arange(len(y))

    if extreme:
        matplotlib.rcParams.update({'font.size': font*10})
        plt.bar(x, y, alpha=0.5)
        ax = plt.gca()
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(base=200))
    else:
        data = pd.DataFrame(data={x_label: x, y_label: y})
        sns.set(style="white", font_scale=font)
        ax = sns.factorplot(x_label, y_label, data=data, kind='bar')

    if ylim:
        ax.set(ylim=(0, ylim))
    
    plt.show()


y = np.array([1,5,10,11])
barPlot(y, 'some categories', 'some value', font=1)
