from rest_framework import serializers
from blog.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedIdentityField(view_name='post_comments_detail')
    body = serializers.HyperlinkedIdentityField(view_name='post_body_detail')

    class Meta:
        model = Post
        fields = '__all__'

class PostBodyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['body']