from django.urls import path

from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('form',views.form,name='form'),
    path('new_page',views.new_page,name='new_page'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('confirm',views.confirm,name='confirm'),
]