from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'owner',)


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')