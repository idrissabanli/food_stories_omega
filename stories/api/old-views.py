from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import ( 
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT
)

from django.http import Http404
from stories.api.serializers import StoryReadSerializer, StoryCreateSerializer
from stories.models import Story


class StoryAPI(APIView):

    def get(self, request, *args, **kwargs):
        stories = Story.objects.all() # ['__all__']
        category = request.GET.get('category') # ?category=2
        tags = request.GET.get('tags') # ?category=2
        if category:
            stories = stories.filter(category__id=category) # filtered stories
        if tags:
            stories = stories.filter(tags__id=tags) # filtered stories
        serializer = StoryReadSerializer(stories, many=True, context={'request': request})
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = StoryCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)


class StoryDetailAPI(APIView):

    def get(self, request, *args, **kwargs):
        story = Story.objects.filter(id=kwargs['pk']).first()
        if not story:
            raise Http404
        serializer = StoryReadSerializer(story, context={'request': request})
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        story = Story.objects.filter(id=kwargs['pk']).first()
        if not story:
            raise Http404
        serializer = StoryCreateSerializer(data=request.data, instance=story)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        story = Story.objects.filter(id=kwargs['pk']).first()
        if not story:
            raise Http404
        serializer = StoryCreateSerializer(data=request.data, partial=True, instance=story)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        deleted_count, _ = Story.objects.filter(id=kwargs['pk']).delete()
        if deleted_count == 0:
            raise Http404
        return Response(data={}, status=HTTP_204_NO_CONTENT)

