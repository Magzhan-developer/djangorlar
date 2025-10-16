from django.db.models import (
    Model,
    CharField,
    IntegerField,
    TextField,
    ForeignKey,
    DateTimeField,
    ManyToManyField,
    BooleanField,
    PositiveIntegerField,
    CASCADE,
)
from django.forms import DecimalField

# Create your models here.
class Cuisine(Model):
    CUISINE_MAX_LENGTH = 100
    name = CharField(
        max_length=CUISINE_MAX_LENGTH,
        unique=True,
        verbose_name="Cuisine Name"
    )

class Category(Model):
    CATEGORY_MAX_LENGTH = 100
    name = CharField(
        max_length=CATEGORY_MAX_LENGTH,
        unique=True,
        verbose_name="Category Name"
    )
    description = TextField(
        null=True,
        blank=True,
    )
    
class Restaurant(Model):
    RESTAURANT_NAME_MAX_LENGTH = 200
    RESTAURANT_ADDRESS_MAX_LENGTH = 200
    RESTAURANT_PHONE_MAX_LENGTH = 20
    
    name = CharField(
        max_length=RESTAURANT_NAME_MAX_LENGTH,
    )
    description = TextField(
        null=True,
        blank=True,
    )
    address = CharField(
        max_length=RESTAURANT_ADDRESS_MAX_LENGTH,
    )
    phone = CharField(
        max_length=RESTAURANT_PHONE_MAX_LENGTH,
        blank=True,
        null=True,
    )
    cuisine = ManyToManyField(
        "Cuisine",
        related_name="restaurants",
    )
    is_active = BooleanField(
        default=True,
    )
    created_at = DateTimeField(
        auto_now_add=True,
    )
    
    
class Option(Model):
    OPTION_NAME_MAX_LENGTH = 100
    name = CharField(
        max_length=OPTION_NAME_MAX_LENGTH,
    )
    price = DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
    )
    is_available = BooleanField(
        default=True,
    )

class Dish(Model):
    DISH_NAME_MAX_LENGTH = 200
    DISH_DESCRIPTION_MAX_LENGTH = 500
    
    name = CharField(
        max_length=DISH_NAME_MAX_LENGTH,
    )
    description = TextField(
        max_length=DISH_DESCRIPTION_MAX_LENGTH,
        null=True,
        blank=True,
    )
    price = DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    options = ManyToManyField(
        "Option",
        blank=True,
        related_name="dishes",
    )
    is_available = BooleanField(
        default=True,
    )
    created_at = DateTimeField(
        auto_now_add=True,
    )
    
class DeliveryZone(Model):  
    ZONE_NAME_MAX_LENGTH = 100
    name = CharField(
        max_length=ZONE_NAME_MAX_LENGTH,
        unique=True,
    )
    restaurant = ForeignKey(
        "Restaurant",
        on_delete=CASCADE,
        related_name="delivery_zones",
    )
    min_order_price = DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    delivery_fee = DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
    )
    estimated_delivery_time = PositiveIntegerField(
        help_text="Estimated delivery time in minutes",
    )
    