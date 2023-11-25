
products = [
    {"product": "leather wallet", "unit price": 1100, "GST": 18, "quantity": 1},
    {"product": "umbrella", "unit price": 900, "GST": 12, "quantity": 4},
    {"product": "cigarette", "unit price": 200, "GST": 28, "quantity": 3},
    {"product": "Honey", "unit price": 100, "GST": 0, "quantity": 2},
]

df = DataFrame(products)


df['total_price'] = df['unit price'] * df['quantity']

df['GST_amount'] = df['total_price'] * (df['GST'] / 100)

total_GST_amount = df['GST_amount'].sum()

max_GST_product = df[df['GST_amount'] == df['GST_amount'].max()]['product'].values[0]

total_amount = df['total_price'].sum()

discounted_products = df[df['unit price'] >= 500]
discounted_products['total_price'] = discounted_products['total_price'] * (1 - 0.05)

total_amount = df['total_price'].sum()

print("Product with maximum GST amount:", max_GST_product)
print("Total amount to be paid:", total_amount)