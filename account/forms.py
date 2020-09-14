from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegistrationUserForm(forms.ModelForm):
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Почта'
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с именем {self.cleaned_data["username"]} уже зарегистрирован.')
        return username


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Имя пользывателя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        cd = self.cleaned_data
        user = authenticate(request=self.request, username=cd['username'], password=cd['password'])
        if user is None:
            raise forms.ValidationError('Неверный логин или пароль')

        cd.update({'user': user})

        return cd
