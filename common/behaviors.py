from django.conf import settings
from django.db import models
from django_extensions.db import fields
from model_utils.managers import PassThroughManager
from common.querysets import AuthorableQuerySet


class Timestampable(models.Model):

    class Meta:
        abstract = True

    created = fields.CreationDateTimeField()
    modified = fields.ModificationDateTimeField()


class Authorable(models.Model):

    class Meta:
        abstract = True

    objects = PassThroughManager.for_queryset_class(AuthorableQuerySet)()

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

