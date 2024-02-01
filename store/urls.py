from django.urls import path
from . import views
from .views import SignUpView
from .views import add_to_cart

app_name = 'store'


urlpatterns = [
    path('',views.products_view,name='products_view'),
    path('products/', views.products_view, name='products_view'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('cart/', views.cart_view, name='cart_view'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

]