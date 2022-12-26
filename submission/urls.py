from django.urls import path 
from . import views
from django.conf.urls.static import static 
from tweetwave.settings import MEDIA_ROOT, MEDIA_URL

app_name = 'submission'

urlpatterns = [
    path('', views.index, name='index'),
    path('confession/', views.saved, name='saved'),
    path('advertising/', views.advertising, name='advertising'),
    path('business/', views.business, name='business'),
    path('about/', views.about, name='about'),
]  + static(MEDIA_URL, document_root=MEDIA_ROOT)