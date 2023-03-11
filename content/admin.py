from django.contrib import admin

from content.models import Catalogue, Song, Genre

admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Catalogue)
