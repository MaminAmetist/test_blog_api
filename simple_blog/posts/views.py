from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import PostDetailSerializer
from .serializers import PostListSerializer
from .serializers import PostCreateUpdateSerializer

from .models import Post


class CreatePostAPIView(CreateAPIView):
    """
    post:
        Creates a new post instance. Returns created post data

        parameters: [title, body, description, image]
    """

    serializer_class = PostCreateUpdateSerializer

    def post(self, request, *args, **kwargs):
        serializer = PostCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class ListPostAPIView(ListAPIView):
    """
    get:
        Returns a list of all existing posts
    """

    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class DetailPostAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a post instance. Searches post using slug field.

    put:
        Updates an existing post. Returns updated post data

        parameters: [slug, title, body, description, image]

    delete:
        Delete an existing post

        parameters = [slug]
    """

    queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostDetailSerializer
