from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('url_shortner.views',
    (r'^$', 'index'),
    (r'^url_handle/$', 'detail'),
    (r'^url_handle/redirect/(\w{4})/$', 'results'),
    (r'^(\w{4})/$','redirect'),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),)
