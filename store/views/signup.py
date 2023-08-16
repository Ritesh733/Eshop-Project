from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View 

class Signup(View):
    ###### GET METHOD #######
    def get(self, request):
        return render(request, 'signup.html')
    
    ###### POST METHOD ######
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
        }

        customers = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password,
                            phone=phone)

        error_message = self.validateCustomer(customers)

        ###### saving ######
        if not error_message:
            print('first_name', 'last_name', 'email', 'password', 'phone')
        # for hash password
            customers.password = make_password(customers.password)
            customers.register()

            return redirect('homepage')
        else:
            data = {'error': error_message,
                'values': value
                }
            return render(request, 'signup.html', data)

    ######## validation #########
    def validateCustomer(self, customers):

        error_message = None

        if not (customers.first_name):
            error_message = "First name required"
        elif not (customers.last_name):
            error_message = "Last name required"
        elif not (customers.email):
            error_message = "Email is required"
        elif not (customers.password):
            error_message = "Password must be 6 letters"
        elif not (customers.phone):
            error_message = "Phone number must be 10 digit required"
        elif customers.isExists():
            error_message = "Email already Exists"
        return error_message
