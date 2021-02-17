from rest_framework import serializers
from .models import Website

class WebsiteSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Website
        fields = '__all__'