# serializers.py
from rest_framework import serializers

from .models import User, Gallery, WeavedImage
from rest_flex_fields import FlexFieldsModelSerializer

class WeavedImageSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = WeavedImage
        fields = ('id','image_name','image_url','image_description','image_creation_time',)

class GallerySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id','gallery_name','weaved_images')
        expandable_fields = {
          'weaved_images': (WeavedImageSerializer, {'many': True})
        }

class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'gallerys')
        expandable_fields = {'gallerys': GallerySerializer}



