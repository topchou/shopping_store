from django.shortcuts import render
from django.http import HttpResponse 
from .models import Product 
from django.template import loader

# use for user register
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

#顯示首頁
def index(request):
    latest_product_list = Product.objects.order_by('-create_date')[:5]
    context ={'latest_product_list': latest_product_list}
    return render(request, 'store/index.html', context)

#顯示產品頁面
def products(request, product_id):
    return HttpResponse("You are looking at %s" %product_id)

# 顯示註冊頁面
def sign_up(request):
    form = CreateUserForm()

    if request.method ==('POST'):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Accou was create for' + user)

    context = {'form': form}
    return render(request, 'store/register.html', context)

#顯示login頁面
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'store/login.html', context)

# logout
def logoutUser(request):
	logout(request)
	return redirect('login')