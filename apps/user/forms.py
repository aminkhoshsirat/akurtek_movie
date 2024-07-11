from django import forms
from .models import *
from django.utils import timezone
from jalali_date import datetime2jalali, date2jalali


def clean_password(password, confirm_password):
    if password == confirm_password:
        if len(confirm_password) > 8 and confirm_password.isdigit() == False and confirm_password.isalpha() == False:
            return confirm_password

        else:
            return ValueError('پسورد باید شامل اعداد  و حروف و نیز بیشتر از 8 کاراکتر باشد')

    else:
        return ValueError('پسورد و تکرار آن یکی نمی باشد')

class UserForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['fullname', 'profile_image', 'birth_date']

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']

        if birth_date == None:
            return birth_date
        
        diff = datetime2jalali(timezone.now()).year - birth_date.year

        if 3 < diff < 130:
            return self.birth_date
        else:
            return ValueError('تاریخ صحیح نمی باشد')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    fullname = forms.CharField(max_length=10000)
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        clean_password(password, confirm_password)


class ResetPasswordSendForm(forms.Form):
    email = forms.EmailField()


class ResetPasswordForm(forms.Form):
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        clean_password(password, confirm_password)
