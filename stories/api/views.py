import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import filters

from rest_framework.status import ( 
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT
)

from django.http import Http404
from stories.api.serializers import StoryReadSerializer, StoryCreateSerializer, SubscriberSerializer
from stories.models import Story, Subscriber

class CustomListCreateAPIView(ListCreateAPIView):

    def get_serializer_class(self):
        print(self.serializer_classes.get(self.request.method))
        return self.serializer_classes.get(self.request.method)


class StoryListCreateAPI(CustomListCreateAPIView):
    queryset = Story.objects.all()
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,  filters.OrderingFilter)
    filter_fields = ('category', 'tags')
    serializer_classes = {
        'GET': StoryReadSerializer,
        'POST': StoryCreateSerializer
    }


class StoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryCreateSerializer


class SubscribersView(CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer