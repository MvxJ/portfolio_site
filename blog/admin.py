from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog.models import Post, Author, Tag

# Register your models here.
class PostAdmin(ModelAdmin):
    readonly_fields = ['slug']
    list_filter =  ('author', 'tags', 'created_at')
    list_display = ('title', 'slug', 'created_at', 'updated_at', 'author')

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
