from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('sign_up/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('sign_in/', views.log_in, name='login')
]
