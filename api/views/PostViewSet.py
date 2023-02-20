from api.models import Post
from rest_framework import viewsets
from api.serializers.PostSerializer import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows post to be viewed or edited.
    """
    view_name = 'post'
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
