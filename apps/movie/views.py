from django.shortcuts import render, get_object_or_404, HttpResponse, Http404
from django.views.generic import View
from apps.panel.models import SiteDetailModel, BannerModel, PrivacyModel, PopularQuestionsModel
from apps.notification.models import NotificationModel
from apps.panel.forms import ContactUsForm
from .models import *


class HeaderView(View):
    def get(self, request):
        site_detail = SiteDetailModel.objects.all().first
        if request.user.is_authenticated:
            notifications = NotificationModel.objects.filter(user=request.user).order_by('-date')
        else:
            notifications = None
        context = {
            'site_detail': site_detail,
            'notifications': notifications
        }
        return render(request, 'partial/header.html', context)


class FooterView(View):
    def get(self, request):
        site_detail = SiteDetailModel.objects.all().first
        context = {
            'site_detail': site_detail,
        }
        return render(request, 'partial/footer.html', context)


class IndexView(View):
    def get(self, request):
        banners = BannerModel.objects.filter(active=True).order_by('-id')
        context = {
            'banners': banners,
        }
        return render(request, 'index.html', context)


class PrivacyView(View):
    def get(self, request):
        site_detail = SiteDetailModel.objects.all().first
        privacy_roles = PrivacyModel.objects.all().order_by('order')
        context = {
            'site_detail': site_detail,
            'privacy_roles': privacy_roles
        }
        return render(request, 'privacy-policy.html', context)


class FaqView(View):
    def get(self, request):
        site_detail = SiteDetailModel.objects.all().first
        popular_questions = PopularQuestionsModel.objects.all().order_by('order')
        context = {
            'site_detail': site_detail,
            'popular_questions': popular_questions,
        }
        return render(request, 'faq.html', context)


class ContactUsView(View):
    def get(self, request):
        site_detail = SiteDetailModel.objects.all().first
        context = {
            'site_detail': site_detail,
        }
        return render(request, 'contact.html', context)

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('ثبت شد')
        else:
            return HttpResponse('مشخضات درست نمی باشد')


class CategoryMainView(View):
    def get(self, request):
        categories = CategoryModel.objects.prefetch_related('category_movies', 'category_series').filter(active=True)
        context = {
            'categories': categories
        }
        return render(request, 'movie/main_category.html', context)


class CategoryView(View):
    def get(self, request, category):
        try:
            item = CategoryModel.objects.prefetch_related('category_series', 'category_movies').get(category=category, active=True)

        except:
            raise Http404
        movies_series = item.category_movies.all() | item.category_movies.all().order_by('-grade')[0:20]
        context = {
            'items': movies_series
        }
        return render(request, 'movie/category.html', context)
