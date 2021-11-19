from rest_framework import serializers
from .models import*


class ShatlSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
        
class CategoryshSerializer(serializers.ModelSerializer):
    model = Aplay
    fields = '__all__'