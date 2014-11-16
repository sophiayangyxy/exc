from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index', name='index'),
    url(r'^post/(?P<post_pk>\d+)/$', 'main.views.detail', name='detail'),
    url(r'^new/', 'main.views.new', name='new'),
    url(r'^delete/(?P<post_pk>\d+)', 'main.views.delete', name='delete'),
    url(r'^edit/(?P<post_pk>\d+)', 'main.views.edit', name='edit'),
)
