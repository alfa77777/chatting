# serializers.py

from rest_framework import serializers
from .models import UserProfile, UserProfileMedia, Post, PostMedia, Comment, Follower, Following, Message, Chat
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(max_length=None, use_url=True, required=False)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'profile_picture', 'birth_date',
                  'address', 'password', 'confirm_password']

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        validated_data.pop('confirm_password', None)
        if password is not None:
            instance.set_password(password)
        return super().update(instance, validated_data)


class UserProfileMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileMedia
        fields = ['id', 'user', 'file', 'created_at', 'expiration_date']


class UserProfileSerializer(serializers.ModelSerializer):
    uploaded_media = UserProfileMediaSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'uploaded_media']


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ['id', 'user', 'file', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    media = PostMediaSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'media', 'content', 'created_at', 'likes', 'comments']


class FollowerSerializer(serializers.ModelSerializer):
    follower = CustomUserSerializer()
    following = CustomUserSerializer()

    class Meta:
        model = Follower
        fields = ['id', 'follower', 'following']


class FollowingSerializer(serializers.ModelSerializer):
    follower = CustomUserSerializer()
    following = CustomUserSerializer()

    class Meta:
        model = Following
        fields = ['id', 'follower', 'following']


class MessageSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'created_at', 'media']


class ChatSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'participants', 'created_at', 'messages']







# # serializers.py
#
# from rest_framework import serializers
# from .models import UserProfile, UserProfileMedia, Post, PostMedia, Comment, Follower, Following, Message, Chat
# from django.contrib.auth.models import User
#
#
# # class UserSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = ['id', 'username']
#
#
# class UserSerializer(serializers.ModelSerializer):
#     profile_picture = serializers.ImageField(max_length=None, use_url=True, required=False)
#     password = serializers.CharField(write_only=True)
#     confirm_password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'profile_picture', 'birth_date',
#                   'address', 'password', 'confirm_password']
#
#     def validate(self, attrs):
#         password = attrs.get('password')
#         confirm_password = attrs.get('confirm_password')
#         if password != confirm_password:
#             raise serializers.ValidationError("Passwords do not match.")
#         return attrs
#
#     def create(self, validated_data):
#         validated_data.pop('confirm_password')
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance
#
#     def update(self, instance, validated_data):
#         password = validated_data.pop('password', None)
#         validated_data.pop('confirm_password', None)
#         if password is not None:
#             instance.set_password(password)
#         return super().update(instance, validated_data)
#
#
# class UserProfileMediaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfileMedia
#         fields = ['id', 'user', 'file', 'created_at', 'expiration_date']
#
#
# class UserProfileSerializer(serializers.ModelSerializer):
#     uploaded_media = UserProfileMediaSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = UserProfile
#         fields = ['user', 'uploaded_media']
#
#
# class PostMediaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostMedia
#         fields = ['id', 'user', 'file', 'created_at']
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#
#     class Meta:
#         model = Comment
#         fields = ['id', 'user', 'content', 'created_at']
#
#
# class PostSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     media = PostMediaSerializer(many=True, read_only=True)
#     comments = CommentSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Post
#         fields = ['id', 'user', 'media', 'content', 'created_at', 'likes', 'comments']
#
#
# class FollowerSerializer(serializers.ModelSerializer):
#     follower = UserSerializer()
#     following = UserSerializer()
#
#     class Meta:
#         model = Follower
#         fields = ['id', 'follower', 'following']
#
#
# class FollowingSerializer(serializers.ModelSerializer):
#     follower = UserSerializer()
#     following = UserSerializer()
#
#     class Meta:
#         model = Following
#         fields = ['id', 'follower', 'following']
#
#
# class MessageSerializer(serializers.ModelSerializer):
#     sender = UserSerializer()
#
#     class Meta:
#         model = Message
#         fields = ['id', 'sender', 'content', 'created_at', 'media']
#
#
# class ChatSerializer(serializers.ModelSerializer):
#     participants = UserSerializer(many=True, read_only=True)
#     messages = MessageSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Chat
#         fields = ['id', 'participants', 'created_at', 'messages']
#
#
#
# # from rest_framework import serializers
# # from django.contrib.auth.models import User
# # from .models import Message
# #
# #
# # # class UserSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = User
# # #         # fields = '__all__'
# # #         fields = ("username", "email", "password", "first_name", "last_name")
# #
# # class UserSerializer(serializers.ModelSerializer):
# #     password = serializers.CharField(write_only=True)
# #
# #     class Meta:
# #         model = User
# #         fields = ("username", "email", "password", "first_name", "last_name")
# #
# #     def create(self, validated_data):
# #         password = validated_data.pop('password')
# #         user = User(**validated_data)
# #         user.set_password(password)
# #         user.save()
# #         return user
# #
# #
# # class UserRetrieveSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = ("username", "email", "first_name", "last_name")
# #
# #
# # class MessageSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Message
# #         fields = '__all__'
