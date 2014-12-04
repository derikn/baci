from django.conf.urls import patterns, url
from login import views

# Class Based Views
urlpatterns = patterns('',
   url('^$', views.HomePageView.as_view(), name='home'),
   url('^login/$', views.LoginView.as_view(), name='login'),
   url('^logout/$', views.LogOutView.as_view(), name='logout'),
   url('^account/$', views.AccountView.as_view(), name='account')
)
