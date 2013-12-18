from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^poll_number_(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^poll_number_(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^poll_number_(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)