from rest_framework import serializers
from api.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'created_at', 'updated_at']
