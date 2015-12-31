from django.conf.urls import include, url
from django.contrib import admin
from store.views import store

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'store.views.index', name='index'),
    url(r'^store/', include('store.urls'), name='store'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('^soc/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
]
