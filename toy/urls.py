from django.urls import path

from . import views

from mysite.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.browse_view),
    path('post', views.create_toy_view),
    path('<int:toy_id>/', views.read_toy_view),
    path('<int:toy_id>/edit', views.update_toy_view),
    path('<int:toy_id>/delete', views.delete_toy_view),
] 
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
   
