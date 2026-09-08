import pandas as pd


def cheque(price_list, **kwargs):
    my_products = sorted(kwargs)
    product_dict = {
        'product': my_products,
        'price': [price_list[i] for i in my_products],
        'number': [kwargs[i] for i in my_products]
    }
    product_dict['cost'] = [price_list[i] * product_dict['number'][ind] for ind, i in enumerate(my_products)]
    s = pd.DataFrame(product_dict)
    return s

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)