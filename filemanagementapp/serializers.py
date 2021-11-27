from django.db import models
from django.db.models import fields
from rest_framework import serializers

from filemanagementapp.models import FileManagement




class FileManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileManagement
        fields = '__all__'