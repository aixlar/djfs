from django.db import models

# Create your models here.

class PizzaShop(models.Model):
    # Fields
    name        = models.CharField(
        verbose_name = 'Pizzeria',
        max_length   = 30,
    )
    description = models.TextField(
        verbose_name = 'Description',
    )
    rating      = models.FloatField(
        verbose_name = 'Rating',
        default      = 0,
    )
    url         = models.URLField(
        verbose_name = 'URL',
    )
    # Meta
    class Meta:
        verbose_name        = 'Pizzeria'
        verbose_name_plural = 'Pizza Shops'
    # Methods
    def __str__(self):
        return self.name


class Pizza(models.Model):
    # Fields
    pizza_shop        = models.ForeignKey(
        PizzaShop,
        on_delete     = models.CASCADE
    )
    name              = models.CharField(
        verbose_name  = 'Name',
        max_length    = 30,
    )
    short_description = models.CharField(
        verbose_name  = 'Short Description',
        max_length    = 30,
    )
    price             = models.IntegerField(
        verbose_name  = 'Price',
        default       = 0,
    )
    photo             = models.ImageField(
        verbose_name  = 'Photo',
        upload_to     = 'firstapp/photos',
        default       = '',
        blank         = True,
    )
    # Meta
    class Meta:
        verbose_name        = 'Pizza'
        verbose_name_plural = 'Pizza Variants'
        ordering            = ['name']
    # Methods
    def __str__(self):
        return self.name
