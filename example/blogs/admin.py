from django.contrib import admin
from .models import post, Document, Comment, Like, Bookmark, Profile, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at']

admin.site.register(post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Document)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Bookmark)
admin.site.register(Profile)
admin.site.site_header = "Blog Admin"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to the Blog Admin Portal"