from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()


class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subscriber(AbsrtactModel):
    email = models.EmailField(_("Email"), unique=True, max_length=50)
    is_active = models.BooleanField('Is Active', default=True)



class Contact(AbsrtactModel):
    SUBJECT_CHOICES = (
        (1, _('Sayt islemir')),
        (2, _('Menimle elaqe saxlayin')),
    )
    name = models.CharField('Ad', max_length=50)
    email = models.EmailField('E Poct', max_length=40)
    subject = models.SmallIntegerField('Movzu', choices=SUBJECT_CHOICES)
    message = models.TextField('Mesaj', help_text='Buraya mesajinizi yazin')

    def __str__(self):
        return self.name


class Category(AbsrtactModel):
    title = models.CharField(max_length=30, help_text='skdfnl')
    image = models.ImageField(upload_to='categories/')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

    @property
    def story_count(self):
        return self.stories.count()


class Tag(AbsrtactModel):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Story(AbsrtactModel):
    category = models.ForeignKey(Category, related_name='stories', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=70, editable=False, db_index=True) 
    image = models.ImageField(upload_to='story_images/')
    cover_image = models.ImageField(upload_to='story_cover_images/')
    content = models.TextField()

    def get_absolute_url(self):
        return reverse_lazy('story_detail', kwargs={
            'slug': self.slug
        })

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title


    

# story = Story.objects.create(category=category, author=user, title='story', image='image.png', cover_image='image.png', content='skjdfdsjkf')
