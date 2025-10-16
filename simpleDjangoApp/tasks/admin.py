from django.contrib import admin

from django.contrib.admin import ModelAdmin, register

# Register your models here.
from tasks.models import Task, UserTask, Project

@register(Task)
class TaskAdmin(ModelAdmin):
    """
    Task admin configuration class.
    """
    
    list_display = (
        "id",
        "name",
        "status",
        "parent",
        "project"
    )
    
    list_display_links = (
        "id",
    )
    list_per_page = 50
    search_fields = (
        "id",
        "name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )
    save_on_top = True
    
    # def has_add_permission(self, request: WSGIRequest) -> bool:
    #     """Disable add permission."""
    #     return False

    # def has_delete_permission(self, request: WSGIRequest, obj: Optional[Project] = None) -> bool:
    #     """Disable delete permission."""
    #     return False

    # def has_change_permission(self, request: WSGIRequest, obj: Optional[Project] = None) -> bool:
    #     """Disable change permission."""
    #     return False

@register(UserTask)
class UserTaskAdmin(ModelAdmin):
    """
    UserTask admin configuration class.
    """
    
@register(Project)
class ProjectAdmin(ModelAdmin):
    """
    Project admin configuration class.
    """

    list_display = (
        "id",
        "name",
        "author",
        "created_at"
    )
    list_display_links = (
        "id",
    )
    list_per_page = 50
    search_fields = (
        "id",
        "name",
    )
    ordering = (
        "-updated_at",
    )
    # list_editable = (
    #     "name",
    # )
    list_filter = (
        # "author",
        "updated_at",
    )

    # fields = (
    #     "name",
    #     "author",
    #     "users",
    # )
    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )
    filter_horizontal = (
        "users",
    )
    save_on_top = True
    fieldsets = (
        (
            "Project Information",
            {
                "fields": (
                    "name",
                    "author",
                    "users",
                )
            }
        ),
        (
            "Date and Time Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                    "deleted_at",
                )
            }
        )
    )
    