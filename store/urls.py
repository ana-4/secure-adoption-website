from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('remove_item/<int:item_id>/', views.removeItem, name='remove_from_cart'),
    path('process_order/', views.processOrder, name="process_order"),
    
]