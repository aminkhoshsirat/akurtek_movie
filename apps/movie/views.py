from django.shortcuts import render, get_object_or_404, HttpResponse, Http404
from django.views.generic import View, DetailView
from apps.panel.models import SiteDetailModel, BannerModel, PrivacyModel, PopularQuestionsModel, TeamMembersModel
from apps.notification.models import NotificationModel
from apps.panel.forms import ContactUsForm
from itertools import chain
from .models import *
from ..user.models import UserModel


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
        movies = MovieModel.objects.all()
        series = SeriesModel.objects.all()
        movie_parts = MoviePartModel.objects.all()
        new_movies = movie_parts.order_by('-id')[0:20]
        movie_likes = movie_parts.order_by('like')[0:20]
        top_series = series.order_by('-grade', '-id')[0:10]
        most_grades = sorted(
            chain(movies, series),
            key=lambda instance: instance.grade,
        )[0:20]
        suggested_for_user = None
        context = {
            'banners': banners,
            'new_movies': movies,
            'movie_likes': movie_likes,
            'top_series': top_series,
            'suggested_for_user': suggested_for_user,
            'most_grades': most_grades,
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


class AboutUsView(View):
    def get(self, request):
        members = TeamMembersModel.objects.filter(is_active=True)
        site_detail = SiteDetailModel.objects.all().first
        context = {
            'members': members,
            'site_detail': site_detail,
            'movie_count': MovieModel.objects.all().count,
            'series_count': SeriesModel.objects.all().count,
            'users_count': UserModel.objects.all().count
        }
        return render(request, 'about-us.html', context)


class CategoryMainView(View):
    def get(self, request):
        categories = CategoryModel.objects.prefetch_related('category_movies', 'category_series').filter(active=True)
        try:
            movies = categories.first().category_movies.all().order_by('-grade')[0:5]
        except:
            movies = None

        try:
            bollywood_movies = categories.filter(url='bollywood').first().category_movies.filter(active=True)[0:20]
        except:
            bollywood_movies = None

        new_series = SeriesModel.objects.all().order_by('-id', '-grade')
        top_turkish_series = SeriesModel.objects.filter(category__url='turkish')

        context = {
            'categories': categories,
            'movies': movies,
            'bollywood_movies': bollywood_movies,
            'new_series': new_series,
            'top_turkish_series': top_turkish_series,
        }
        return render(request, 'movie/main_category.html', context)


class CategoryView(View):
    def get(self, request, category):
        try:
            item = CategoryModel.objects.prefetch_related('category_series', 'category_movies').get(id=category, active=True)

        except:
            raise Http404
        movies_series = item.category_movies.all() | item.category_movies.all().order_by('-grade')[0:20]

        context = {
            'items': movies_series
        }
        return render(request, 'movie/category.html', context)


class MovieBaseView(DetailView):
    template_name = 'movie/movie-base.html'
    slug_field = 'url'
    model = MovieModel
    context_object_name = 'movie'
    queryset = MovieModel.objects.all()

    def get_queryset(self):
        return MovieModel.objects.prefetch_related('movie_parts').filter(active=True)


class MovieDetailView(DetailView):
    template_name = 'movie/movie-details.html'
    slug_field = 'url'
    model = MoviePartModel
    context_object_name = 'movie'
    queryset = MoviePartModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        category = context.get('movie').base.category.all()
        print(category)
        if category:
            movies = MoviePartModel.objects.filter(base__category__in=category)
        else:
            movies = None
        context['new_movies'] = movies[0:20]
        context['similar_movies'] = movies.order_by('-base__grade')[0:20]
        return context


class SeriesBaseView(DetailView):
    template_name = 'movie/series-base.html'
    slug_field = 'url'
    model = SeriesModel
    context_object_name = 'seri'

    def get_queryset(self):
        return SeriesModel.objects.prefetch_related('series_season', 'series_season__season_parts').filter(active=True)


class SerialDetailView(DetailView):
    template_name = 'movie/series-details.html'
    slug_field = 'url'
    model = SeriesPartModel
    context_object_name = 'seri'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['season'] = SeriesSeasonModel.objects.prefetch_related('season_parts').filter(series__active=True)
        return context



