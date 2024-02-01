
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse



def products_view(request):
    return render(request, 'store/products.html')


@login_required
def cart_view(request):
    return render(request, 'store/cart.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def pay_and_order(request):
    if request.method == 'POST':
        # Kullanıcıdan gelen bilgileri işle

        messages.success(request, 'Order successfully placed!')
        return redirect('store:products_view')

    return render(request, 'store/cart.html') 

# views.py

from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Product, Order

def add_to_cart(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse("Ürün bulunamadı!")  # veya başka bir hata mesajı veya yönlendirme

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']

            # Siparişi oluştur
            order = Order.objects.create(
                product=product,
                fullname=fullname,
                address=address,
                phone_number=phone_number
            )

            return render(request, 'order_confirmation.html', {'order': order})

    else:
        form = OrderForm()

    return render(request, 'add_to_cart.html', {'form': form, 'product': product})
