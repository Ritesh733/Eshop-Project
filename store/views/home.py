from django.shortcuts import render
from store.models.category import Category
from store.models.product import Product


# Create your views here.


def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    print('you are :', request.session.get('email'))

    # return render(request, 'orders/order.html')
    return render(request, 'index.html', data)