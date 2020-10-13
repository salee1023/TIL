# 1. Django Core
from django.shortcuts import get_object_or_404
from rest_framework import serializers
# 2. Third Party
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# 3. Local Files
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    # 조회, 수정, 삭제할 데이터 가져오기 
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)  # 포맷 변환
        # print(serializer.data)
        # print(type(serializer))
        return Response(serializer.data)  # 응답
    elif request.method == 'PUT':
        # 수정할 인스턴스, 사용자가 요청 보낸 데이터 넣어주기
        serializer = ArticleSerializer(instance=article, data=request.data)  
        # 유효성 검사 후 이상 없으면 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)  # 수정된 데이터 응답
    else:
        # 삭제하기
        article.delete()
        # 메시지 응답
        return Response({'message': f'{article_pk}번 글이 정상적으로 삭제되었습니다.'})


@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)  # 포맷 변환
        return Response(serializer.data)  # 응답

    elif request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)  
        # 유효성 검사 후 이상 없으면 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)  # 수정된 데이터 응답
    else:
        # 삭제하기
        comment.delete()
        # 메시지 응답
        return Response(
            {'message': f'{comment_pk}번 글이 정상적으로 삭제되었습니다.'},
            stauts=status.HTTP_204_NO_CONTENT # comment가 없을 때 출력해줄 내용
            )