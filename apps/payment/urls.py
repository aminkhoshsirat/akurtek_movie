from django.urls import path
from .views import *

app_name = 'payment'

urlpatterns = [
    path('', PricingPlanView.as_view(), name='index'),
    path('buy/<pk>', BuyPlanView.as_view(), name='buy'),
]
