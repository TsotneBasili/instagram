from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", 'username', 'email']


class PostSerializer(serializers.ModelSerializer):
    model = Post
    user = UserSerializer(read_only=True)
    field = ["id", "title", "body", "user", "slug"]
