from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('hackathon.urls', namespace='hackathon')),
    url(r'^admin/', include(admin.site.urls)),
)
