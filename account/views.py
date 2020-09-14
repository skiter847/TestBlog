from django.shortcuts import render, redirect
from .forms import RegistrationUserForm
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

            return redirect("blog:post_list")

    return render(request, 'account/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect("account:login")
