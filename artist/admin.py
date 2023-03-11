from django.contrib import admin
from reports.base import reports

from artist.models import Artist, ArtistReport

admin.site.register(Artist)
reports.register(Artist, ArtistReport)
