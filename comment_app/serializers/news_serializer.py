from comment_app.models import News
from rest_framework import serializers
from .comment_serializer import CommentSerializer
from fluent_comments.models import FluentComment

class NewsSerializer(serializers.ModelSerializer):
     comments= serializers.SerializerMethodField()
    
     class Meta:
          model = News
          fields = ('title','details','comments')
    
     def get_comments(self,obj):
          news_comment = FluentComment.objects.filter(object_pk = obj.id, parent_id = None)
          serializer = CommentSerializer(news_comment,many=True)
          return serializer.data

     def create(self, validated_data):
          #Edit
          news = News(**validated_data)
          news.save()
          return news

     