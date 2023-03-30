from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from item.models import Item, Category
from .forms import SignUpForm, LoginForm


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('core:index')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form, 'title': 'Sign Up'})
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:index')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form, 'title': 'Login'})