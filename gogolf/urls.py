from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gogolf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello-world/$', 'golfApp.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)