from rest_framework import serializers
from .models import BlogCategory, Post, BlogComment, BlogMedia
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'title', 'description', 'thumbnail', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()
    audios = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'category', 'thumbnail', 'images', 'videos', 'audios']

    def get_images(self, obj):
        """
        Get serialized images related to the given post.
        """
        images = obj.get_images()
        return [image.media_file.url for image in images]

    def get_videos(self, obj):
        """
        Get serialized videos related to the given post.
        """
        videos = obj.get_videos()
        return [video.media_file.url for video in videos]

    def get_audios(self, obj):
        """
        Get serialized audios related to the given post.
        """
        audios = obj.get_audios()
        return [audio.media_file.url for audio in audios]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ['id', 'author', 'post', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogMedia
        fields = '__all__'
