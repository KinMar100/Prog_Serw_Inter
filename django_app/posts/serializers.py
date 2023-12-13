from . models import Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'description',
            'add_date',
            'edit_date',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'post',
            'description',
            'add_date',
            'edit_date',
        ]
