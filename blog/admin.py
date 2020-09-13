from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'publish', 'created', 'updated')
    prepopulated_fields = {'slug': ('title', )}