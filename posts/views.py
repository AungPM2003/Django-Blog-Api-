from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from posts.models import Post
from posts.serializers import PostSerializer
# Create your views here.

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer