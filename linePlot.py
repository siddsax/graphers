import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

hour, direction = np.meshgrid(np.arange(24), np.arange(1,3))
df = pd.DataFrame({"hour": hour.flatten(), "direction": direction.flatten()})
df["hourly_avg_count"] = np.random.randint(14,30, size=len(df))


font=1.5
sns.set(style="white", font_scale=font)
x = np.array([5, 10, 20, 30, 5, 10, 20, 30])#.reshape((2, 4))
y = np.array([28.37, 30.97, 33.03, 33.27, 30.14, 33.21, 36.06, 38.06])#.reshape((2,4))
z = ['MLN', 'MLN', 'MLN' , 'MLN', 'MLN-SS', 'MLN-SS', 'MLN-SS', 'MLN-SS']
df = pd.DataFrame({'Precision @1' : x, 'Models': z, 'Percentage Data': y})
plt.figure(figsize=(12,8))
sns.tsplot(df, time='Precision @1', unit = "Models", 
               condition='Models', value='Percentage Data')

plt.title('Precision score on NUS-WIDE')

plt.show()
