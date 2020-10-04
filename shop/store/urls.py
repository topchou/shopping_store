from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.index, name="index"),
    path('<int:product_id>/',views.products, name="products"),
] 
