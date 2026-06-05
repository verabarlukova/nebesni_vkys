from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from .models import Product, Order, Client

# --- Просмотр меню (ВАЖНО: класс должен быть выше, чем функции) ---
class ProductListView(ListView):
    model = Product
    template_name = 'core/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = self.kwargs.get('category')
        if category:
            return Product.objects.filter(category=category)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        context['cart_count'] = len(cart)
        return context

# --- Корзина ---
def cart_view(request):
    cart_ids = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart_ids)
    total_price = sum(p.price for p in products)
    return render(request, 'core/cart.html', {
        'products': products, 
        'total_price': total_price
    })

# --- Добавление в корзину ---
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', [])
    cart.append(product.id)
    request.session['cart'] = cart
    return redirect('product_list')

# --- Оформление заказа ---
def create_order(request):
    if request.method != 'POST':
        return redirect('cart_view')

    cart_ids = request.session.get('cart', [])
    if not cart_ids:
        return redirect('cart_view')
    
    client = Client.objects.first()
    if not client:
        client = Client.objects.create(
            name="Гость", 
            phone="80000000000", 
            address="Адрес не указан"
        )
    
    products = Product.objects.filter(id__in=cart_ids)
    total = sum(p.price for p in products)
    
    order = Order.objects.create(
        address=client.address,
        status="Новый",
        total_price=total,
        order_type="Доставка",
        client=client
    )
    order.items.set(products)
    request.session['cart'] = []
    
    return render(request, 'core/order_success.html', {'order_id': order.id})