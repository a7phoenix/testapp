from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


def upload_location(instance, filename, **kwargs):
    file_path = 'archive/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path

class Tag(models.Model):
    text = models.CharField(max_length=100, unique=True)

class NewsModel(models.Model):
    title = models.CharField(max_length=50, null=False, blank=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    tags = models.ManyToManyField(Tag, related_name='spot_facilities', null=True, blank=True)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=NewsModel)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_blog_post_receiever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiever, sender=NewsModel)