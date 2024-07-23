from django.shortcuts import render, HttpResponse, redirect, Http404, get_object_or_404
from django.views.generic import View
from utils.send_email import send_activation_code
from django.contrib.auth import login, logout
from django.utils.crypto import get_random_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import datetime
from apps.panel.models import SiteDetailModel
from redis import Redis
from .forms import *

re = Redis(host='localhost', port=6379, db=0)


class ManageProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserForm(instance=request.user)
        user = request.user
        if user.pricing:
            if user.pricing > datetime.now():
                pricing_amount = user.pricing - datetime.now()
            else:
                pricing_amount = None
        else:
            pricing_amount = None

        site_detail = SiteDetailModel.objects.all().first()
        context = {
            'form': form,
            'pricing_amount': pricing_amount,
            'site_detail': site_detail,
        }
        return render(request, 'user/manage-profile.html', context)

    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            cd = form.cleaned_data
            user.fullname = cd['fullname']
            user.birth_date = cd['birth_date']
            user.profile_image = cd['profile_image']
            user.save()
        return redirect('user:manage_profile')


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = UserModel.objects.get(email=cd['email'])
            if user:
                check = user.check_password(cd['password'])
                if check:
                    login(request, user)
                    return redirect(request.META['HTTP_REFERER'])
                else:
                    return HttpResponse('پسورد اشتباه است')
            else:
                return HttpResponse('کاربر یافت نشد')


class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('movie:index')


class SignUpView(View):
    def get(self, request):
        return render(request, 'user/sign-up.html')

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = UserModel.objects.filter(email=cd['email'])
            if user.exists():

                if user.first().ban:
                    return HttpResponse('کاربر مسدود شده است')
                elif user.is_active:
                    return HttpResponse('کاربر با این مشخصات وجود دارد')
                else:
                    code = get_random_string(72)
                    request.session['user_email'] = user.email
                    re.set(f'activation_code:{user.email}', code, ex=3600)
                    send_activation_code(user.email, code)
                    return HttpResponse('برای فعال سازی خساب ایمیل خود را چک کنید')

            else:
                UserModel.objects.create_user(email=cd['email'], fullname=cd['fullname'], password=cd['password'])
                code = get_random_string(72)
                request.session['user_email'] = user.email
                re.set(f'activation_code:{user.email}', code, ex=3600)
                send_activation_code(user.email, code)
                return HttpResponse('برای فعال سازی خساب ایمیل خود را چک کنید')


class ActivationView(View):
    def get(self, request, code):
        email = request.sessin['email']
        user = get_object_or_404(UserModel, email=email)
        if user.is_active:
            return render(request, 'user/activation.html', {'message': 'کاربر قبلا فعال شده'})
        else:
            user_code = re.get(f'activation_code:{user.email}')
            if user_code == code:
                user.is_active = True
                user.save()
                return render(request, 'user/activation.html', {'message': 'کاربر فغال شد'})
            else:
                raise Http404


class ResetPasswordSendView(View):
    def get(self, request):
        return render(request, 'user/reset-password-send.html')

    def post(self, request):
        form = ResetPasswordSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = UserModel.objects.filter(email=cd['email'])
            if user.exists():
                if user.first().ban:
                    return HttpResponse('کاربر مسدود شده')

                else:
                    code = get_random_string(72)
                    re.set(f'reset-code:{user.email}', code, ex=3600)
                    request.session['email'] = user.email
                    send_activation_code(user.email, code)
                    return HttpResponse('code send')
            else:
                return HttpResponse('کاربر با ایمیل وجود ندارد')


class ResetPasswordView(View):
    def get(self, request, code):
        email = request.session.get('email')
        send_code = re.get(f'reset-code:{email}')
        if code == send_code:
            return render(request, 'user/reset-password.html')
        else:
            raise Http404()

    def post(self, request, code):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = request.session.get('email')
            send_code = re.get(f'reset-code:{email}')
            user = UserModel.objects.filter(email).first()
            if user:
                if code == send_code:
                    cd = form.cleaned_data
                    user.set_password(cd['password'])
                    user.save()
                    return HttpResponse('پسورد تغییر یافت')

            else:
                return HttpResponse('کاربر یافت نشد')