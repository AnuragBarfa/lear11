from django.conf.urls import url
from . import views
app_name = 'student'
urlpatterns = [
    #url(r'^notes/$', views.notes,name='notes'),
    url(r'^notes/$', views.all_semester, name='all_semester'),
    url(r'^notes/add/$',views.add_notes,name='add_notes')
]
urlpatterns+=[
    url(r'^notes/(?P<Semester_name>[\w\-]+)/$', views.all_subjects_in_semester, name='all_subjects_in_semester'),
    url(r'^notes/(?P<Semester_name>[\w\-]+)/(?P<Subject_name>[\w\-]+)/$', views.all_notes_in_subject, name='all_notes_in_subject')
]