from django.conf.urls import url
from . import views

app_name = 'alumni'
urlpatterns = [
    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^video/upload/$',views.video_upload,name='video_upload'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^post/approval/$',views.post_approval,name="post_approval"),
    url(r'^post/(?P<pk>\d+)/approve/$', views.post_approve, name='post_approve'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
urlpatterns+=[
    url(r'^alumni/$', views.alumni_list, name='alumni_list'),
    url(r'^alumni/(?P<pk>\d+)/$', views.alumni_detail, name='alumni_detail'),
]
