from typing import Any
from django.db import models
from django.utils import timezone as django_timezone
# Create your models here.
class AbstractSoftDeletableModel(models.Model):
    """
    Abstract soft-deletable model with common fields.
    """
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Timestamp when the record was soft-deleted.",
    )
    
    def soft_delete(self,*args:tuple[Any,...], **kwargs:dict[str,Any]) -> None:
        """Soft delete the object by setting deleted_at timestamp."""
        self.deleted_at = django_timezone.now()
        self.save(update_fields=['deleted_at'])
    
    class Meta:
        """Meta class for AbstractSoftDeletableModel."""
        abstract = True
    