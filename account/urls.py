from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('sign_up/', views.register, name='login'),
    path('logout/', views.logout, name='logout'),
    path('sign_in/', views.log_in, name='login')
]
