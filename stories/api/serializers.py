from rest_framework import serializers
from stories.models import Story, Category, Tag, Subscriber

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 
            'title',
            'image',
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title'
        )


class StoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = (
            'category',
            'author',
            'tags',
            'title',
            'slug',
            'image',
            'cover_image',
            'content',
            'created_at',
            'updated_at',
        )




class StoryReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    # created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Story
        fields = (
            'id',
            'category',
            'author',
            'tags',
            'title',
            'slug',
            'image',
            'cover_image',
            'content',
            'created_at',
            'updated_at',
        )


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )