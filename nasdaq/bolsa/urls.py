from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^bovespa/$', views.bovespa_upload, name='upload'),# isto realiza o upload dos chamados
    url(r'^fibo/$', views.stock, name='fibo'),
    url(r'^fibonacci/$', views.fibonacci, name='fibonacci'),
    url(r'^download/$', views.excel_download, name='download'),
    url(r'^delete/$', views.showthis, name='showthis'),
]
