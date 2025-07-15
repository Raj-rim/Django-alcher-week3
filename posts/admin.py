from django.contrib import admin
from .models import Post, Cast

class CastInline(admin.TabularInline):  
    model = Cast
    extra = 1 

class PostAdmin(admin.ModelAdmin):
    inlines = [CastInline]

admin.site.register(Post, PostAdmin)