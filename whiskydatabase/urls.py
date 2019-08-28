from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from whiskydatabase.views import  HomeView, WhiskyView, DistilleryMapView, WhiskyListView, BarMapView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^distillery_map/$', DistilleryMapView.as_view(), name='distillery_map'),
    url(r'^bar_map/$', BarMapView.as_view(), name='bar_map'),
    url(r'^whisky_gallery/$', WhiskyListView.as_view(), name='whisky_list'),
    url(r'^whisky/(?P<whisky_slug>[-\w]+)/$', WhiskyView.as_view(), name='whisky_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)