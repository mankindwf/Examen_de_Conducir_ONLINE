from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^vigos/', include('django.contrib.auth.urls')),
    url(r'^vigos/', include('quiz.urls')),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

