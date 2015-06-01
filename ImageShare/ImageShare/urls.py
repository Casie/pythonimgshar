from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
import settings
import views

from shareimg import urls as appurls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ImageShare.views.home', name='home'),
    # url(r'^ImageShare/', include('ImageShare.foo.urls')),
    url(r'^$', views.index, name="main"),
    url(r'^upload/$', views.handle_upload, name="upload"),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(appurls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
