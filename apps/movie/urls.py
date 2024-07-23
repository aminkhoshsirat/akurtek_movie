from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category', CategoryMainView.as_view(), name='main_category'),
    path('category/<category>', CategoryView.as_view()),
    path('privacy-policy', PrivacyView.as_view(), name='privacy'),
    path('faq', FaqView.as_view(), name='faq'),
    path('contact-us', ContactUsView.as_view(), name='contact_us'),
    path('about-us', AboutUsView.as_view(), name='about_us'),
    path('movie/<slug>', MovieBaseView.as_view(), name='movie_base'),
    path('movie-detail/<slug>', MovieDetailView.as_view(), name='movie_detail'),
    path('series/<slug>', SeriesBaseView.as_view(), name='series_base'),
    path('series-detail/<slug>', SerialDetailView.as_view(), name='series_detail'),
]
