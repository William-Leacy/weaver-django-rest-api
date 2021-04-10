# serializers.py
from rest_framework import serializers

from .models import WeaverUser, WeavedImage
from rest_flex_fields import FlexFieldsModelSerializer

class WeavedImageSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = WeavedImage
        fields = "__all__"  

class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = WeaverUser
        fields = ('user_id','email', 'weaved_images')
        expandable_fields = {'weaved_images': WeavedImageSerializer}
