from django.urls import path 
from . import views
from django.conf.urls.static import static
from tweetwave.settings import MEDIA_ROOT, MEDIA_URL

app_name = 'moderator' 

urlpatterns = [
    path('', views.index, name='index'),
    path('approve/<str:uuid>/', views.approve, name='approve'),
    path('remove/<str:uuid>/', views.remove, name='remove'),
    path('approved/', views.approved, name='approved'),
    path('pending/', views.pending, name='pending'),
    path('flagged/', views.flagged, name='flagged'),
    path('adverts/', views.adverts, name='adverts'),
    path('contact/<str:uuid>', views.contact, name='contact'),
    path('reject/<str:uuid>', views.reject, name='reject'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
