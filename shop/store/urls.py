from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('register/', views.sign_up, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    # path('logout/', views.logoutUser, name="Logout"),
    path('',views.index, name="index"),
    path('<int:product_id>/',views.products, name="products"),
] 
