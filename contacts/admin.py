from django.contrib import admin
from django.utils.html import format_html
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profile_picture_tag', 'video_tag', 'created_at')

    def profile_picture_tag(self, obj):
        """Show profile picture thumbnail in admin list."""
        if obj.profile_picture:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:5px;" />',
                obj.profile_picture.url
            )
        return "No Image"
    profile_picture_tag.short_description = 'Profile Picture'

    def video_tag(self, obj):
        """Show clickable video link in admin list."""
        if obj.video:
            return format_html(
                '<a href="{}" target="_blank">View Video</a>',
                obj.video.url
            )
        return "No Video"
    video_tag.short_description = 'Video'
