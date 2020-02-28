# б) Задача. Визначити кількість товарів, які продані менш ніж рік тому і вивести
# відомості про них. Поля структури: Продавець, Найменування товару, Кількість, Ціна,
# Дата продажу.
# Васильченко Даниїл Назарович 1 курс група 122A
products = [{'seller': 'ahmid', 'product_name': 'bread', 'count': 2, 'cost': 1, 'date_of_sale': 2019},
            {'seller': 'petrik', 'product_name': 'bread', 'count': 5, 'cost': 1, 'date_of_sale': 1941},
            {'seller': 'midjit', 'product_name': 'bread', 'count': 3, 'cost': 1, 'date_of_sale': 1488},
            ]

count_of_products_type = len(products)
elements = []
all_count = 0
for i in range(0, len(products)):
    date = products[i].get('date_of_sale')
    if 2020 - date <= 1:
        all_count += products[i].get('count')
        elements.append(i)
for i in elements:
    print(f'products by the desired date: {products[i]}')
print(f'count of all products by the desired date: {all_count}')
