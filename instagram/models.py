# models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone
from datetime import timedelta


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='users_custom', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='users_custom', blank=True)


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    uploaded_media = models.ManyToManyField('UserProfileMedia', blank=True)


class UserProfileMedia(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.expiration_date = timezone.now() + timedelta(hours=24)
        super(UserProfileMedia, self).save(*args, **kwargs)


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    media = models.ManyToManyField('PostMedia', blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts')
    comments = models.ManyToManyField(CustomUser, through='Comment', related_name='commented_posts')


class PostMedia(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_follower')
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='follower_set')


class Following(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_following')
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following_set')


class Chat(models.Model):
    participants = models.ManyToManyField(CustomUser, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='chat_media/', null=True, blank=True)


# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.utils import timezone
# from datetime import timedelta
#
#
# class User(AbstractUser):
#     username = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     address = models.CharField(max_length=255, null=True, blank=True)
#     groups = models.ManyToManyField(Group, related_name='users_custom', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='users_custom', blank=True)
#
#     password = models.CharField(max_length=128)
#     confirm_password = models.CharField(max_length=128)
#
#     # Override the save() method to handle password hashing
#     def save(self, *args, **kwargs):
#         if self.password and self._state.adding:
#             self.set_password(self.password)
#         super().save(*args, **kwargs)
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     uploaded_media = models.ManyToManyField('UserProfileMedia', blank=True)
#
#
# class UserProfileMedia(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='media/')
#     created_at = models.DateTimeField(auto_now_add=True)
#     expiration_date = models.DateTimeField()
#
#     def save(self, *args, **kwargs):
#         self.expiration_date = timezone.now() + timedelta(hours=24)
#         super(UserProfileMedia, self).save(*args, **kwargs)
#
#
# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     media = models.ManyToManyField('PostMedia', blank=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     likes = models.ManyToManyField(User, related_name='liked_posts')
#     comments = models.ManyToManyField(User, through='Comment', related_name='commented_posts')
#
#
# class PostMedia(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='media/')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#
# class Follower(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_follower')
#     follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_set')
#
#
# class Following(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_following')
#     following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
#
#
# class Chat(models.Model):
#     participants = models.ManyToManyField(User, related_name='chats')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#
# class Message(models.Model):
#     chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
#     sender = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     media = models.FileField(upload_to='chat_media/', null=True, blank=True)
#
#
#
# # from django.db import models
# # from django.contrib.auth.models import User
# #
# #
# # class Message(models.Model):
# #     objects = None
# #     sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
# #     receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
# #     content = models.TextField()
# #     timestamp = models.DateTimeField(auto_now_add=True)
# #
# #     class Meta:
# #         verbose_name = 'Message'
# #         verbose_name_plural = 'Messages'
# #         ordering = ['-timestamp']
# #
# #
# # class UserProfile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     # Add any additional user profile fields you need
# #
# #     class Meta:
# #         verbose_name = 'User Profile'
# #         verbose_name_plural = 'User Profiles'
# #
