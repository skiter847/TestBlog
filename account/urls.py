from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('sign_in/', views.login, name='login')
]
