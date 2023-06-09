from django.contrib import admin
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
router.register(r'users', UserViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]


# # urls.py
#
# from django.contrib import admin
# from django.urls import include, path
# from rest_framework import routers
# from .views import (
#     UserProfileViewSet,
#     UserProfileMediaViewSet,
#     PostViewSet,
#     PostMediaViewSet,
#     CommentViewSet,
#     FollowerViewSet,
#     FollowingViewSet,
#     UserViewSet,
# )
#
# router = routers.DefaultRouter()
# router.register(r'user-profiles', UserProfileViewSet)
# router.register(r'user-profile-media', UserProfileMediaViewSet)
# router.register(r'posts', PostViewSet)
# router.register(r'post-media', PostMediaViewSet)
# router.register(r'comments', CommentViewSet)
# router.register(r'followers', FollowerViewSet)
# router.register(r'followings', FollowingViewSet)
# router.register(r'users', UserViewSet)
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
# ]


# from django.contrib import admin
# from django.urls import include, path
# from rest_framework import routers
# from .views import PostViewSet, CommentViewSet, UserViewSet, FollowViewSet
#
#
# router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet)
# router.register(r'comments', CommentViewSet)
# router.register(r'users', UserViewSet)
# router.register(r'follows', FollowViewSet)
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
# ]
#




# from django.urls import path
# from .views import UserListCreateView, UserRetrieveUpdateDestroyView, \
#     MessageListCreateView, MessageRetrieveUpdateDestroyView
#
# urlpatterns = [
#     path('users/', UserListCreateView.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
#     path('messages/', MessageListCreateView.as_view(), name='message-list'),
#     path('messages/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view(), name='message-detail'),
# ]
