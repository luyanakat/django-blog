from django.urls import path

from . import views


urlpatterns = [
    path('posts/', views.PostAPIView.as_view(), name='list-posts'),
    path('posts/<int:id>/', views.PostAPIView.as_view(), name='detail-posts'),
]