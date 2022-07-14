from rest_framework import serializers
from django.db.models import fields
from api.models import ImageFile  # import model


# Create a class
class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = '__all__'
