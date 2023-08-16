from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View 

class Login(View):
    ########### GET Method login
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        ########### POST Method login
    
        email = request.POST.get('email')
        password = request.POST.get('password')
        customers = Customer.get_customer_by_email(email)
        error_message = None
        
        ########## This code below check password
        if customers:
            flag = check_password(password, customers.password)
            if flag:
                request.session['customers'] = customers.id
                request.session['email'] = customers.email
                return redirect('homepage')
            else:
                error_message = 'Email or Password invailid'
        else:
            error_message = 'Email or Password invailid'
        
        ######## Now this code below through error if emasil or password is incorrect
        print(email, password, customers)
        return render(request, 'login.html', {'error': error_message})    
