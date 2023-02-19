from api.models import Comment
from rest_framework import viewsets
from api.serializers.CommentSerializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Comment to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
