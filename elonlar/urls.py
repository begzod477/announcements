from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, announcement_detail, select_by_category

urlpatterns = [
    path('', home, name='home'),
    path('announcement/<int:id>/', announcement_detail, name='announcement_detail'),
    path('category/<int:category_id>/', select_by_category, name='select_by_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
