from django.urls import path

from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("login", views.login_user, name="login_user"),
    path("register",views.register_user, name="register_user"),
    path("faqs", views.faqs, name="faqs"),
    path("product", views.product, name="product"),
    path("cart", views.cart, name="cart"),
    path("add-to-cart/<int:id>", views.add_to_cart, name="add_to_cart"),
    path("checkout", views.checkout, name="checkout")
]