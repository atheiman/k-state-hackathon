from django.conf.urls import patterns, url

from .views import index, register, team, edit_team, review

urlpatterns = patterns('',
    # /
    url(r'^\/?$', index, name='index'),

    # /register
    url(r'^register\/?$', register, name='register'),

    # /team/1
    url(r'^team/(?P<team_id>\d+)\/', team, name='team'),

    # /team/1/edit
    url(r'^team/(?P<team_id>\d+)/edit\/', edit_team, name='edit_team'),

    # /vote
    url(r'^review\/?$', review, name='review'),
)
