from rest_framework import serializers
from .models import ProductCategory, Product, ProductComment, ProductMedia


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'title', 'description', 'thumbnail','created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()
    audios = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'category', 'price', 'thumbnail', 'images', 'videos', 'audios')

    def get_price(self, obj):
        return obj.price().price

    def get_images(self, obj):
        """
        Get serialized images related to the given product.
        """
        images = obj.get_images()
        return [image.media_file.url for image in images]

    def get_videos(self, obj):
        """
        Get serialized videos related to the given product.
        """
        videos = obj.get_videos()
        return [video.media_file.url for video in videos]

    def get_audios(self, obj):
        """
        Get serialized audios related to the given product.
        """
        audios = obj.get_audios()
        return [audio.media_file.url for audio in audios]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = ['id', 'author', 'product', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = '__all__'
