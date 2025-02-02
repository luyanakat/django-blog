from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from utils.response import custom_response

from .models import Posts
from .serializers import PostSerializer


@api_view(['GET'])
def get_list(request):
    """Lấy danh sách tất cả bài viết"""
    posts = Posts.objects.all()
    serializer = PostSerializer(posts, many=True)
    return custom_response(data=serializer.data)


@api_view(['GET'])
def get_by_id(request, id):
    """Lấy một bài viết theo ID"""
    post = get_object_or_404(Posts, id=id)
    serializer = PostSerializer(post)
    return custom_response(data=serializer.data)


@api_view(['POST'])
def create_post(request):
    """Tạo một bài viết mới"""
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return custom_response(data=serializer.data)
    return custom_response(data=serializer.errors, code=status.HTTP_400_BAD_REQUEST)
