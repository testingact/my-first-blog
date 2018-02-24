from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.menu, name='menu'),
    url(r'^setting/$', views.setting, name='setting'),
    url(r'^result/(?P<pk>\d+)/$', views.result_detail, name='result_detail'),
    url(r'^crawling/list/$', views.crawling_list, name='crawling_list'),
    url(r'^export/csv/(?P<pk>\d+)/$', views.export_csv, name='export_csv'),
    url(r'^file/$', views.file_input, name='file_input'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^crawling/new/$', views.crawling_input, name='crawling_input'),
    #url(r'^crawling/(?P<pk>\d+)/$', views.crawling_detail, name='crawling_detail'),
    #url(r'^search-form/$', views.search_form),
    #url(r'^search/$', views.search),
]