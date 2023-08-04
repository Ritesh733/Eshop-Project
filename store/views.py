from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
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
    # print(prd)
    # return render(request, 'orders/order.html')
    return render(request, 'index.html', data)

def signup(request):
    
    customer = None

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        print('first_name', 'last_name', 'email', 'password', 'phone')
        
        
        customer = Customer(
            first_name = first_name,
            last_name = last_name,
            email  =email,
            password = password,
            phone = phone
            )
        customer.save()
        # return HttpResponse('Form submitted successfully....')
    else:
        return render(request, 'signup.html', customer)