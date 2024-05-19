def orders_list():
    orders = [{
        'stoks': 'first',
        'quantity': 100
    },
    {
        'stoks': 'second',
        'quantity': 200
    },
    {
        'stoks': 'third',
        'quantity': 300
    },
    {
        'stoks': 'fourth',
        'quantity': 400
    },
    {
        'stoks': 'fifth',
        'quantity': 500
    }
    ]
    return orders


def single_order():
    order = {
        'stoks': 'some_stock',
        'quantity': 123
    }
    return order


def incorrect_single_order():
    order = "{ 'stoks': 'some_stock', 'quantity': 123"
    return order

def url_address():
    url = 'http://server:8080'
    return url
