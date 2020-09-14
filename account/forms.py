from django import forms
from django.contrib.auth.models import User


class RegistrationUserForm(forms.ModelForm):
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Имя пользывателя',
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
