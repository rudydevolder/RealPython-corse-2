from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', 'helloworld.views.hello_view'),
    url(r'^$', 'helloworld.views.hello_view'),
    url(r'^better/$', 'helloworld.views.better_hello')
)
