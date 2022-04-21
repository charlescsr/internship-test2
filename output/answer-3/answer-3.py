import pandas as pd

df = pd.read_csv('/home/csr/Documents/internship-test2/input/question-3/main.csv')
df.head()

df.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False, inplace=True)

cols = ['Team', 'Red Cards', 'Yellow Cards']
df = df[cols]

df.to_csv('main.csv', index=False)