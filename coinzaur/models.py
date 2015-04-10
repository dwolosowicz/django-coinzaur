from django.contrib.auth.models import AbstractUser
from django.db import models
from timezone_field import TimeZoneField


class CoinzaurUser(AbstractUser):
    timezone = TimeZoneField(default="Europe/Warsaw")

    currency = models.CharField(max_length=32, default="PLN")

    income = models.DecimalField(max_digits=10, decimal_places=2, default=2000)