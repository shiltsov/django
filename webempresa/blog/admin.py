from django.contrib import admin
from .models import Post, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'author','post_categories')
    ordering = ('title','author', '-published')
    search_fields = ('title','content','author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'категории'

admin.site.register(Post, PostAdmin)       