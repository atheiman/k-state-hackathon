from django.conf.urls import patterns, url

from .views import index, register_user, register_team, vote

urlpatterns = patterns('',
    # /
    url(r'^\/?$', index, name='index'),

    # /register/user
    url(r'^register/user\/?$', register_user, name='register_user'),

    # /register/team
    url(r'^register/team\/?$', register_team, name='register_team'),

    # /vote
    url(r'^vote\/?$', vote, name='vote'),
)
