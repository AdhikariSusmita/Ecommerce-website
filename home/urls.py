from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('brand/<slug>', BrandView.as_view(), name='brand'),
    path('search', SearchView.as_view(), name='search'),
    path('product_detail/<slug>', ProductDetailView.as_view(), name='product_detail'),
    path('signup', signup, name='signup'),
    path('product_review/<slug>', ProductDetailView.as_view(), name='product_review'),
    path('cart', CartView.as_view(), name='cart'),
    path('count_cart', count_cart, name='count_cart'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('reduce_quantity/<slug>', reduce_quantity, name='reduce_quantity'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    path('wish', WishlistView.as_view(), name='wish'),
    path('count_wish', count_wishlist, name='count_wish'),
    path('add_to_wishlist/<slug>', add_to_wishlist, name='add_to_wishlist'),
    path('reduce_quantity/<slug>', reduce_quantity, name='reduce_quantity'),
    path('delete_wishlist/<slug>', delete_wishlist, name='delete_wishlist'),
]
