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
]
