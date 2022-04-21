import pandas as pd

df = pd.read_csv('/home/csr/Documents/internship-test2/input/question-1/main.csv')
df.head()

df['price_new'] = df.groupby('product_description')['price'].transform('mean')

df.head()

df.to_csv('main.csv', index=False)