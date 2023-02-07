from django.urls import path, include
from rest_framework import routers
from api.views import (
    UserViewSet,
    GroupViewSet,
    PostViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet.UserViewSet, basename='users')
router.register(r'groups', GroupViewSet.GroupViewSet, basename='groups')
router.register(r'posts', PostViewSet.PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls))
]
