from rest_framework import serializers
from .models import Automobile, Part, File


class AutomobileSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Automobile
        fields = '__all__'


class PartSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class FileSerilizers(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
