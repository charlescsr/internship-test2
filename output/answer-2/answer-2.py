import pandas as pd

df = pd.read_csv('/home/csr/Documents/internship-test2/input/question-2/main.csv')
df.head()

def convert_to_kg(row):
    if row['product_description'] == 'milk-1.5':
        return row['sales_quantity'] * 1.5

    elif row['product_description'] == 'butter-0.25':
        return row['sales_quantity'] * 0.25
    
    else:
        return row['sales_quantity']

df['sales_quant_new'] = df.apply(convert_to_kg, axis=1)

df['sales_amount'] = df['price'] * df['sales_quant_new']

df.drop(columns=['sales_quant_new'], inplace=True)

df.to_csv('main.csv', index=False)