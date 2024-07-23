from django.contrib import admin
from django.urls import path, include
from azbankgateways.urls import az_bank_gateways_urls
from apps.payment.views import GoToGetAwayView, CallbackGetAwayView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.movie.urls', namespace='movie'), name='movie'),
    path('user/', include('apps.user.urls', namespace='user'), name='user'),
    path('blog/', include('apps.blog.urls', namespace='blog'), name='blog'),
    path('chat/', include('apps.chat.urls', namespace='chat'), name='chat'),
    path('panel/', include('apps.panel.urls', namespace='panel'), name='panel'),
    path('notification/', include('apps.notification.urls', namespace='notification'), name='notification'),
    path('payment/', include('apps.payment.urls', namespace='payment'), name='payment'),
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-get-away/', GoToGetAwayView.as_view()),
    path('callback-get-away/', CallbackGetAwayView.as_view()),
]
