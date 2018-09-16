import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
# # Load iris data
# titanic = sns.load_dataset("titanic")

# # Construct iris plot
# g = sns.factorplot("class", "survived", "sex", data=titanic, kind="bar", palette="muted", legend=True)
# # Show plot
def plotBar1(y, x_label, y_label, x=None, title=None, font=1, ylim=0):
    if x is None:
        x = np.arange(len(y))
    data = pd.DataFrame(data={x_label: x, y_label: y})
    sns.set(style="white", font_scale=font)
    # tips = sns.load_dataset("tips")
    lm = sns.factorplot(x_label, y_label, data=data, kind='bar')
    # axes = lm.axes
    if ylim:
        lm.set(ylim=(0, ylim))
    plt.show()

# y = [.01, .4, .004, .9, .5]
# plotBar1(y, 'asd', 'www', font=1.5)
