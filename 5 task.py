
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 1 point
df = pd.DataFrame(np.random.randint(1, 11, size=100).reshape((10, 10)))
print(df, end='\n\n')

# 2 point
df.index = ('A B C D E F G H I J'.split())
print(df, end='\n\n')
for i in range(10):
    df = df[df[i] > 5]
print(df)

# 3 point
matr = pd.DataFrame(10*np.random.random((10, 10)).round(3))
matr.index = 'A B C D E F G H I J'.split()
matr.columns = 'A B C D E F G H I J'.split()
print(matr, end='\n\n')
print(f'{len(matr.index)} x {len(matr.columns)}', end='\n\n')
print(matr.to_numpy().sum()/matr.size, end='\n\n')
matr.to_csv('numbs.csv')

#
emoj = pd.read_csv('emojis.csv', parse_dates=True)
b = emoj.groupby('Category')['Rank'].sum()
print(b, '\n\n')
ind = b[b == b.min()].index
print(ind)

# 5 point
a = emoj.groupby('Year')['Year'].count()
print(a)
plt.plot(emoj.groupby('Year')['Year'].count())
plt.show()
# почему не работает ?


