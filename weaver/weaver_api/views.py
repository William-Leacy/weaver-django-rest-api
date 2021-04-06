from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer, GallerySerializer, WeavedImageSerializer
from .models import User, Gallery, WeavedImage


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class WeavedImageViewSet(viewsets.ModelViewSet):
    queryset = WeavedImage.objects.all()
    serializer_class = WeavedImageSerializer
