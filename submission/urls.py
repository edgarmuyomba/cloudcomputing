from django.urls import path 
from . import views
from tweetwave.settings import MEDIA_ROOT, MEDIA_URL
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'submission'

urlpatterns = [
    path('', views.index, name='index'),
    path('confession/', views.saved, name='saved'),
    path('advertising/', views.advertising, name='advertising'),
    path('business/', views.business, name='business'),
    path('about/', views.about, name='about'),
]  + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)