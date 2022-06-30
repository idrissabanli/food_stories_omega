from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from stories.api.serializers import StoryReadSerializer
from drf_yasg.utils import swagger_serializer_method

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    stories = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'stories',
            'email',
            'username'
        )

    @swagger_serializer_method(StoryReadSerializer(many=True))
    def get_stories(self, obj):
        serializer = StoryReadSerializer(obj.stories.all(), many=True)
        return serializer.data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs=attrs)
        user_serializer = UserSerializer(self.user)
        data.update(user_serializer.data)
        return data
