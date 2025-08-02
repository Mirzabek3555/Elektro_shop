from django.urls import path
from main.views import index, products, register, user_login

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('products/<int:id>/', products, name='products'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
