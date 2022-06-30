from django.urls import path
from stories.views import (
    home, recipes,
    export,
    stories, StoryDetailView,
    ContactView,
    CreateStoryView,
    UpdateStoryView,
    StoryListView,
    like_story,
    liked_stories
)


urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipes, name='recipes_page'),
    path('stories/', StoryListView.as_view(), name='stories_page'),
    path('create-story/', CreateStoryView.as_view(), name='create_story'),
    path('update-story/<int:pk>/', UpdateStoryView.as_view(), name='update_story'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('liked-stories/', liked_stories, name='liked_stories'),
    path('like/<int:id>/', like_story, name='like_story'),
    path('stories/<slug:slug>/', StoryDetailView.as_view(), name='story_detail'),
    path('export/', export, name='export'),
]