from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('',views.index , name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),



]