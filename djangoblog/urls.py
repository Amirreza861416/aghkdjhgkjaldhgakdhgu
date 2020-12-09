from django.contrib import admin
from django.urls import path , include
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

urlpatterns = [
    path('manage-admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login),
    path('info/', views.info),
    path('register/', views.register),
    path("users/", include('acc.urls')),
    path('users/',include('django.contrib.auth.urls')),
    path("", include('django_messages.urls')),
    path('access/', views.access),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('simplegame/', views.games),

]

from mafiaapp import views
urlpatterns += [
    url(r'^game/',views.index, name='index'),
    url(r'^(?P<game_id>\w+)/$', views.lobby,name='lobby'),
    url(r'^(?P<game_id>\w+)/game/$', views.ingame, name='ingame'),
    url(r'^api/createlobby', views.createlobby, name='createlobby'),
    url(r'^api/joinlobby', views.joinlobby, name='joinlobby'),
    url(r'^api/removeuser', views.removeuser, name='removeuser'),
    url(r'^api/startgame', views.startgame, name='startgame'),
    url(r'^api/endround',views.endround, name='endround'),
    url(r'^api/leavegame',views.leavegame, name='leavegame'),
    url(r'^api/getusers',views.getusers,name='getusers'),
    url(r'^api/getround',views.getround,name='getround'),
    url(r'^api/leavelobby',views.leavelobby,name='leavelobby'),
    url(r'^api/startround',views.startround,name='startround'),

]

urlpatterns += staticfiles_urlpatterns()
handler404 = 'djangoblog.views.notfound'
