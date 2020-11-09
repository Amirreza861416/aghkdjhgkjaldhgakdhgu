from django.urls import path , include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.articles_list),
    url(r'^$', views.ListCourse.as_view(), name='course_list'),
]
