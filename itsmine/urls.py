from django.conf.urls import url
from . import views

app_name='itsmine'

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^reg$',views.reg,name='reg'),
    url(r'^login$',views.logi,name='login'),
]