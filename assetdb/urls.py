from __future__ import absolute_import

from django.conf.urls import patterns, url, include
from assetdb import views

urlpatterns = patterns ('',
	#assetURLs
	url(r'^$', views.AssetListView.as_view(), name='list'),
	url(r'^d/(?P<pk>\d+)/$', views.AssetDetailView.as_view(), name='detail'),
	url(r'^create/$', views.AssetCreateView.as_view(), name='create'),
	url(r'^e/(?P<pk>\d+)/$', views.AssetUpdateView.as_view(), name='update'),
	url(r'^del/(?P<pk>\d+)/$', views.AssetDeleteView.as_view(),
        name='delete'),
	)