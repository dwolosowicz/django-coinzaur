from django.db import models
from django_extensions.db import fields

from .auth import CoinzaurUser
from common.behaviors import Timestampable, Authorable


class Tag(Timestampable, Authorable, models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    label = models.CharField(max_length=255)


class Expense(Timestampable, Authorable, models.Model):
    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    tags = models.ManyToManyField(Tag)

    title = models.CharField(max_length=255)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def products_cost(self):
        return sum(p.cost for p in self.product_set.all())

    def not_specified_cost(self):
        return self.total_cost - self.products_cost()

    def __unicode__(self):
        return unicode(self.title)


class Product(Timestampable, models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    expense = models.ForeignKey(Expense)

    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return unicode(self.name)