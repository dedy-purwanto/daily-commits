from django.conf.urls.defaults import patterns, url
from .views import MainView


urlpatterns = patterns('frontend.views',
    url(r'^$', MainView.as_view(), name='home'),
)
