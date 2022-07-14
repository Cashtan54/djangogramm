from django.contrib import admin

from .models import User, Post, Image, Tag


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'last_login',
        'is_superuser',
        'username',
        'is_staff',
        'is_active',
        'date_joined',
        'email',
        'slug',
        'bio',
        'profile_photo',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )
    raw_id_fields = ('groups', 'user_permissions')
    search_fields = ('slug',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_date', 'text')
    list_filter = ('user', 'created_date')
    raw_id_fields = ('likes', 'tags')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'post')
    list_filter = ('post',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
