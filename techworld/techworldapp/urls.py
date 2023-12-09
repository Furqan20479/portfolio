
from django.urls import path
from . import views

urlpatterns = [

 
    path('',views.base_view, name='base'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
    

]
