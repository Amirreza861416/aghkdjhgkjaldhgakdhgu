from django.contrib import admin
from django.urls import path , include
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path("rooms/", views.rooms),
    path("users/", include('acc.urls')),
    path('users/',include('django.contrib.auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api/v1/courses/', include('articles.urls', namespace='course')),

]

urlpatterns += staticfiles_urlpatterns()
handler404 = 'djangoblog.views.notfound'
