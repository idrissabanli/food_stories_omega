from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from stories.models import Story
from slugify import slugify



# @receiver(pre_save, sender=Story)
# def story_object_creation(sender, instance, **kwargs):
#     instance.slug = f"{slugify(instance.title)}-{instance.id}"
#     # instance.save()

@receiver(post_save, sender=Story)
def story_object_creation(sender, instance, created, **kwargs):
    print(created)
    old_slug = instance.slug
    new_slug = f"{slugify(instance.title)}-{instance.id}"
    if  created and old_slug != new_slug:
        instance.slug = new_slug
        instance.save()
        print('isledi')

# @receiver(pre_save, sender=Recipe)
# def story_object_creation(sender, **kwargs):

