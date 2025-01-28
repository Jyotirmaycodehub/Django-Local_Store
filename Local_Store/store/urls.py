# from django.urls import path
# from .views import product_list, product_detail

# urlpatterns=[
#     path('', product_list, name='product_list'),
#     path('product/<int:pk>/', product_detail, name='product_detail'),
#     path('add_to_cart/<int:pk>/', add_to_cart_view, name='add_to_cart'),

# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('sotre.urls')),
# ]

