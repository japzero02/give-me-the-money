from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_student$', display_student, name='display_student'),
]