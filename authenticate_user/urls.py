from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .views import SignUpViewSet
router = DefaultRouter()
router.register('signup', SignUpViewSet, base_name='signup')
urlpatterns = [

    path('', include(router.urls))

] + static(settings.MEDIA_URL, document_url=settings.MEDIA_ROOT)
