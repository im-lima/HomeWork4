from django.contrib import admin
from posts.models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "rate", "created_at", "updated_at")
    search_fields = ("title", "description")

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)