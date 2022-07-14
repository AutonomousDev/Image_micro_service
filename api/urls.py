
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
router = DefaultRouter(trailing_slash=False)

router.register(r'image_file', views.ImageFileViewSet,basename="image_file"),

urlpatterns = [
    path('', include(router.urls)),
]