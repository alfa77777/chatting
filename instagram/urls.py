from django.urls import include, path
from rest_framework import routers
from .views import (
    UserProfileViewSet,
    UserProfileMediaViewSet,
    PostViewSet,
    PostMediaViewSet,
    CommentViewSet,
    FollowerViewSet,
    FollowingViewSet,
    UserViewSet,
    ChatViewSet,
    MessageViewSet
)

router = routers.DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'user-profile-media', UserProfileMediaViewSet)
router.register(r'posts', PostViewSet)
router.register(r'post-media', PostMediaViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'followers', FollowerViewSet)
router.register(r'followings', FollowingViewSet)
router.register(r'user', UserViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('instagram_api/', include(router.urls)),
]
