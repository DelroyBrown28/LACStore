from django.contrib import admin
from django.urls import include, path
from products import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.all_products, name='products'),


]
