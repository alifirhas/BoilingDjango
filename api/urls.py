from django.urls import path, include
from rest_framework import routers
from api.views import (
    UserViewSet,
    GroupViewSet,
    PostViewSet,
)
from api.views import CommentViewSet
# Register new viewSet above

router = routers.DefaultRouter()
router.register(r'users', UserViewSet.UserViewSet, basename='users')
router.register(r'groups', GroupViewSet.GroupViewSet, basename='groups')
router.register(r'posts', PostViewSet.PostViewSet, basename='posts')
router.register(r'comments', UserViewSet.UserViewSet, basename='Comments')
# Register new view above

urlpatterns = [
    path('', include(router.urls))
]
