# views.py

from rest_framework import viewsets
from .models import UserProfile, UserProfileMedia, Post, PostMedia, Comment, Follower, Following, Chat, Message
from .serializers import (
    UserProfileSerializer,
    UserProfileMediaSerializer,
    PostSerializer,
    PostMediaSerializer,
    CommentSerializer,
    FollowerSerializer,
    FollowingSerializer,
    CustomUserSerializer,
    ChatSerializer,
    MessageSerializer,
)
from django.contrib.auth.models import User


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileMediaViewSet(viewsets.ModelViewSet):
    queryset = UserProfileMedia.objects.all()
    serializer_class = UserProfileMediaSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostMediaViewSet(viewsets.ModelViewSet):
    queryset = PostMedia.objects.all()
    serializer_class = PostMediaSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FollowerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer


class FollowingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer











# from rest_framework import viewsets
# from .models import Post, Comment, Follow
# from .serializers import PostSerializer, CommentSerializer, FollowSerializer, UserSerializer
# from django.contrib.auth.models import User
#
#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class FollowViewSet(viewsets.ModelViewSet):
#     queryset = Follow.objects.all()
#     serializer_class = FollowSerializer











# from rest_framework import generics
# from django.contrib.auth.models import User
# from .models import Message
# from .serializers import UserSerializer, MessageSerializer, UserRetrieveSerializer
#
#
# class UserListCreateView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return UserSerializer
#         return UserRetrieveSerializer
#
# # class UserListCreateView(generics.ListCreateAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer
#
#
# class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class MessageListCreateView(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#
#
# class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
