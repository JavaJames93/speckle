from django.conf.urls import url

from . import views

urlpatterns = [
    #/finance/
    url(r'^$', views.index, name='index'),

    #/finance/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    #/finance/webscraping
    url(r'^webscraper/$', views.webscraper, name='webscraper')
]
