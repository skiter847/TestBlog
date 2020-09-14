from django.shortcuts import render, redirect, reverse
from .forms import RegistrationUserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


# Create your views here.
def register(request):
    form = RegistrationUserForm()
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = User.objects.create(username=cd['username'], email=cd['email'], is_staff=True)
            new_user.set_password(cd['password'])
            new_user.save()

            return redirect("account:login")

    return render(request, 'account/register.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect("account:login")


def log_in(request):
    form = LoginUserForm(request)

    if request.method == 'POST':
        form = LoginUserForm(request, request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['user']:
                login(request, cd['user'])

            return redirect("blog:post_list")

    return render(request, 'account/login.html', {
        'form': form
    })
