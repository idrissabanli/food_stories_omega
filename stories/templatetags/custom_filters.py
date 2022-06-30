from django.template import Library
from stories.models import Category

register = Library()

@register.filter
def split_by(string, value=' '):
    return string.split(value)
