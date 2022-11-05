"""samakdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from email.mime import base
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, contact_view, about_view, social_view
from products.views import dynamic_lookup_view, product_create_view
from products.views import product_list_view, product_details_view, product_delete_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home_view, name='home'),
    path('travello/', include('travello.urls')),
    path('contact/', contact_view, name='contact'),
    path('social/', social_view),
    path('about/', about_view),
    
    path('product/', product_details_view),
    path('product/<int:my_id>/', dynamic_lookup_view),
    path('product/<int:id>/delete/', product_delete_view),
    path('create/', product_create_view),
    path('product_list/', product_list_view),
    
    path('blog/', include('blog.urls')),
    
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
