from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet,RatingViewSet,UserViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]