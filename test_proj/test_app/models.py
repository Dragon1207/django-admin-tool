from admin_tools.db.fields import GenericForeignKey
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Bar(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Foo(models.Model):
    name = models.CharField(max_length=100, null=True)
    bar = models.ForeignKey(Bar, models.SET_NULL, null=True,
                            related_name='foos')

    def __str__(self):
        return self.name


class Baz(models.Model):
    name = models.CharField(max_length=100, null=True)
    foos = models.ManyToManyField(Foo, related_name='bazes', blank=True)
    content_type = models.ForeignKey(ContentType, models.SET_NULL, blank=True,
                                     null=True, related_name='+')

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)

    def __str__(self):
        return self.title


def get_related_models():
    return (Blog, Bar, Baz)


class Comment(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.CASCADE, blank=True, null=True,
        related_name='comments'
    )

    owner_id = models.IntegerField(null=True, blank=True)
    owner_content_type = models.ForeignKey(
        ContentType, models.CASCADE, related_name='+', null=True, blank=True
    )
    owner = GenericForeignKey(
        ct_field='owner_content_type',
        fk_field='owner_id',
        related_models=get_related_models
    )

    def __str__(self):
        return self.title
