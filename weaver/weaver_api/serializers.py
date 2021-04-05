# serializers.py
from rest_framework import serializers

from .models import User, Gallery, WeavedImage

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username',)

class GallerySerializer(serializers.HyperlinkedModelSerializer):
    user_gallery = UserSerializer(many=True)
    class Meta:
        model = Gallery
        fields = ('name','user_gallery')

class WeavedImageSerializer(serializers.HyperlinkedModelSerializer):
    gallery_image = GallerySerializer(many=True)
    class Meta:
        model = WeavedImage
        fields = ('id','gallery','gallery_image','image_name','image_url','image_description','image_creation_time')