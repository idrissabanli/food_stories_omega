from django.template import Library
from stories.models import Category

register = Library()


@register.simple_tag
def get_categories(offset, limit, order):
    if order > 0:
        return Category.objects.all().order_by('created_at')[offset:limit]
    return Category.objects.all().order_by('-created_at')[offset:limit]
