from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_student$', display_student, name='display_student'),
    url(r'^add_student$', add_student, name="add_student"),
    url(r'^edit_student/(?P<pk>\d+)$', edit_student, name='edit_student'),
    url(r'^delete_student/(?P<pk>\d+)$', delete_student, name='delete_student'),
    url(r'^upload_csv$', upload_csv, name='upload_csv'),
]
