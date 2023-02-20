from api.models import Like
from rest_framework import viewsets
from api.serializers.LikeSerializer import LikeSerializer


class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Like to be viewed or edited.
    """
    queryset = Like.objects.all().order_by('-created_at')
    serializer_class = LikeSerializer
