from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.landing,name='landing'),
    url(r'^index', views.index, name='index'),
    url(r'leaderboard$', views.leaderboard, name='leaderboard'),
    url(r'^api/quest/$', views.TournamentList.as_view()),
    url(r'api/quest/quest-id/(?P<pk>[0-9]+)/$',
        views.TournamentDescription.as_view()),
    url(r'^new/tournament$',views.new_tournament,name='new-tournament'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)