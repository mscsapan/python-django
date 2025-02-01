"""
URL configuration for my_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from  product import product_views
from all_views.cart import cart_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('add/', views.add_person ,name='add'),
    path('add-person/', views.add_new_person ,name='add-person'),
    path('edit-person/<int:id>', views.edit_person ,name='edit-person'),
    path('update-person/<int:id>', views.update_person ,name='update-person'),
    path('delete-person/<int:id>', views.delete_person ,name='delete-person'),
    
    
    path('product/', product_views.product,name='product'),
    path('cart/', cart_views.my_cart,name='cart'),
    
    # path('api/home', include()),
]
