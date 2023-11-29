from django.http import JsonResponse


"""
Вьюха get_products_view должна возвращать список продуктов, если обратиться по адресу http://127.0.0.1:8000/products/
Но в некоторых ситуациях, там хотелось бы получать продукты только одного типа, для этого можно использовать GET параметры.
Например по адресу http://127.0.0.1:8000/products/?type=books получить только продукты с типом книнги

Задания:
    1. Напишите логику во вьюхе get_products_view таким образом, что если в пути есть параметр type, то должны
       возвращаться только продукты определенного типа.
    2. Если параметра type нет, должны возвращаться все продукты.
    3. Файл urls.py трогать не нужно, праметры хранятся в объекте request.
"""
PRODUCTS = [
    {'type': 'electronics', 'title': 'Smartphone', 'price': 500},
    {'type': 'clothing', 'title': 'T-Shirt', 'price': 20},
    {'type': 'books', 'title': 'Python for Beginners', 'price': 25},
    {'type': 'electronics', 'title': 'Television', 'price': 300},
    {'type': 'clothing', 'title': 'Sneakers', 'price': 50},
    {'type': 'groceries', 'title': 'Milk', 'price': 2},
    {'type': 'toys', 'title': 'Lego Set', 'price': 40},
    {'type': 'books', 'title': 'Django for Dummies', 'price': 30},
    {'type': 'electronics', 'title': 'Laptop', 'price': 1000},
    {'type': 'clothing', 'title': 'Jeans', 'price': 40},
    {'type': 'groceries', 'title': 'Eggs', 'price': 3},
    {'type': 'toys', 'title': 'Action Figure', 'price': 15},
    {'type': 'home & garden', 'title': 'Lawn Mower', 'price': 250},
    {'type': 'electronics', 'title': 'Headphones', 'price': 100},
    {'type': 'clothing', 'title': 'Jacket', 'price': 60},
    {'type': 'home & garden', 'title': 'Chair', 'price': 80},
    {'type': 'books', 'title': 'JavaScript: The Good Parts', 'price': 35},
    {'type': 'groceries', 'title': 'Bread', 'price': 1},
    {'type': 'toys', 'title': 'Board Game', 'price': 25},
    {'type': 'home & garden', 'title': 'Table', 'price': 120}
]


def get_products_view(request):
    type_ = request.GET.get('type')
    products = []
    if type_ is None:
        products = PRODUCTS
    else:
        products = list(filter(lambda product: product['type'] == type_, PRODUCTS))
    result = {'count': len(products), 'products': products}
    return JsonResponse(data=result, safe=False)
