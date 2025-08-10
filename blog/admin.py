from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified',)
    ordering = ('status', 'datetime_modified', )
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'body', 'active', 'date_time_created']
    ordering = ['date_time_created', ]