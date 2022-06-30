from django.urls import path
from stories.api.views import (
    StoryListCreateAPI, 
    StoryRetrieveUpdateDestroyAPIView, 
    SubscribersView,
)
urlpatterns = [
    path('stories/', StoryListCreateAPI.as_view(), name='api_stories'),
    # path('list-stories/', StoryListAPI.as_view(),),
    path('stories/<int:pk>/', StoryRetrieveUpdateDestroyAPIView.as_view(),),
    path('subscribers/', SubscribersView.as_view(),)
]