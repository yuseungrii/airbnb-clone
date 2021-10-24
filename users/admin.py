from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User) #모델 가져오기
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    #    list_display = ("username", "email", "gender", "currency", "superhost")
    #    list_filter = ("language", "currency", "superhost")

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
