from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'content', 'article']
        # 필드를 추가하거나 재정의하지않으면 shortcut 사용 가능
        read_only_fields = ['article',] 


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'title',]


class ArticleSerializer(serializers.ModelSerializer):
    # 필드를 추가하거나 재정의하면 각 필드에 read_only=True 사용
    comment_set = CommentSerializer(
        many=True, read_only=True
        ) 
    comment_count = serializers.IntegerField(
        source='comment_set.count', read_only=True
        )

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ['id', 'title', ' content', 'comment_set','comment_count',]
        
