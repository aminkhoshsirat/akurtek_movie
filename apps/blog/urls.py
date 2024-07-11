from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('category/<category>', BlogView.as_view(), name='category'),
    path('tag/<tag>', BlogView.as_view(), name='tag')
]