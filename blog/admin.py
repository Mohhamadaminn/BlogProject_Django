from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified',)
    ordering = ('status', 'datetime_modified', )
    