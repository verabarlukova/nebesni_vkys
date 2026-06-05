from django.urls import path
from . import views

urlpatterns = [
    # Используем .as_view(), так как это класс
   path('', views.ProductListView.as_view(), name='product_list'),
   path('category/<str:category>/', views.ProductListView.as_view(), name='category_list'),
   path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
   path('cart/', views.cart_view, name='cart_view'),
   path('create-order/', views.create_order, name='create_order'),
]