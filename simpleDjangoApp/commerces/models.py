from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField,
    DateTimeField,
    FloatField,
    DecimalField,
    ManyToManyField,
    TextField,
    BooleanField,
    PositiveIntegerField
)
from django.contrib.auth.models import User



# Create your models here.
class Cart(Model):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="carts",
        )
    created_at = DateTimeField(
        auto_now_add=True
        )
    updated_at = DateTimeField(
        auto_now=True
    )
    
class CardItem(Model):
    cart = ForeignKey(
        "Cart",
        related_name="items",
        on_delete=CASCADE
    )
    dish = ForeignKey(
        "Dish",
        related_name="dishes",
        on_delete=CASCADE
    )
    quantity = PositiveIntegerField(
        default=1
    )
    
class PromoCode(Model):
    PROMO_CODE_MAX_LENGTH = 20
    DESCRIPTION_MAX_LENGTH = 200
    
    code = CharField(
        unique=True,
        max_length=PROMO_CODE_MAX_LENGTH
    )
    description = TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        blank=True,
        null=True
    )
    discount_percentage = PositiveIntegerField(
        default=0
    )
    valid_from = DateTimeField()
    valid_until = DateTimeField()
    is_active = BooleanField(
        default=True
    )
    