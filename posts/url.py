from django.urls import path
from posts.views import get_list, get_by_id, create_post

urlpatterns = [
    path('posts/', get_list, name='post-list'),  # Lấy danh sách bài viết
    path('posts/<int:id>/', get_by_id, name='post-detail'),  # Lấy bài viết theo ID
    path('posts/create', create_post, name='post-create'),  # Tạo bài viết mới
]
