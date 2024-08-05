from django.contrib import admin

# Register your models here.

from .models import Media, Tag

admin.site.register(Media)
admin.site.register(Tag)
