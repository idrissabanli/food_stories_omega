from modeltranslation.translator import translator, TranslationOptions
from stories.models import Story

class StoryTranslationOption(TranslationOptions):
    fields = ('title', 'slug', 'content')


translator.register(Story, StoryTranslationOption)