from posts.models import Posts
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Title must be at least 10 characters long')
        return value