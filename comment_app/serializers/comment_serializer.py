from rest_framework import serializers
from fluent_comments.models import FluentComment

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(
            value,
            context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    
    class Meta:
        model = FluentComment
        fields = (
            'comment',
            'id',
            'children',
           )