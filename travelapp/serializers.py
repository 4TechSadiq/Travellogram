from rest_framework import serializers
from .models import DestinationData

class GetForm(serializers.ModelSerializer):
    picture = serializers.ImageField(required=False)
    class Meta:
        model = DestinationData
        fields = '__all__'
        read_only_fields = ['place_name']