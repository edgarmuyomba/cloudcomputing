from django.urls import path, include
from . import views
from tweetwave.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]  + static(MEDIA_URL, document_root=MEDIA_ROOT)