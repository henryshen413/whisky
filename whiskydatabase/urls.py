from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from whiskydatabase.views import HomeView, WhiskyView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    url(r'^whisky/(?P<whisky_slug>[-\w]+)/$', WhiskyView.as_view(), name='whisky')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)