from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer, GallerySerializer, WeavedImageSerializer
from .models import User, Gallery, WeavedImage


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username',)
    serializer_class = UserSerializer

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('user',)
    serializer_class = GallerySerializer

class WeavedImageViewSet(viewsets.ModelViewSet):
    queryset = WeavedImage.objects.all().order_by('image_url',)
    serializer_class = WeavedImageSerializer
