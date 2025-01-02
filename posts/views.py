from rest_framework import generics, status
from rest_framework.views import APIView

from posts.models import Posts
from posts.serializers import PostSerializer
from rest_framework.response import Response

# Create your views here.
class PostAPIView(APIView):
    from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Posts
from .serializers import PostSerializer

class PostAPIView(APIView):
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('id') 
        
        if post_id:  
            try:
                post = Posts.objects.get(id=post_id)
                serializer = PostSerializer(post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Posts.DoesNotExist:
                return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        else: 
            posts = Posts.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        # Tạo bài viết mới
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        