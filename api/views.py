from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from api.models import ImageFile
from rest_framework import viewsets
from api.serializers import ImageFileSerializer


class ImageFileViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing images.
    """
    queryset = ImageFile.objects.all()
    serializer_class = ImageFileSerializer
