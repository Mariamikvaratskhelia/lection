from django.contrib import admin
from .models import Movie,IMDBRating,Album,Song,Actor

admin.site.register(Movie)
admin.site.register(IMDBRating)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Actor)
