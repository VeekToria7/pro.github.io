from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User

from .form import RegistrationForm

from django.contrib.auth import login, authenticate

from .models import Category, Product, Profile, Cart

# Create your views here.
def home(request):
    all_categories = Category.objects.all()

    return render(request, "store/project.html",{"all_categories":all_categories})

def about(request):
    return render(request, "store/project_about.html")

def contact(request):
    return render(request, "store/pro_contact.html")

def login_user(request):

    msg = ""
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
           
            return redirect('home')
        
        else:
            msg = "Invalid username or password"

    return render(request,"store/login.html",{'msg':msg})

def register_user(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()

            return redirect('login_user')
        else:
            return render(request,"store/register.html",{'form':form})
        
    form = RegistrationForm()
    return render(request,"store/register.html",{'form':form})

def faqs(request):
    return render(request, "store/faQs.html")

def cart(request):
    try:
        user = User.objects.get(id=request.user.id)
        user_cart = Cart.objects.filter(user=user)
        return render(request, "store/carts.html", {'user_cart':user_cart})
    except User.DoesNotExist:
        return redirect("login_view")

def product(request):
    all_category = Category.objects.all()
    products = Product.objects.all()

    return render (request, "store/product.html", {'all_product':products,'all_category':all_category})


def add_to_cart(request,id):
    product = Product.objects.get(id=id)
    new_cart = Cart()

    new_cart.user = request.user
    new_cart.product = product

    new_cart.save()

    return redirect('cart')

def checkout(request):
    return render(request, "store/check_out.html")