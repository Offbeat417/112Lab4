from django.contrib import admin
from .models import Genre, Movie

# Create Admin templates for the models
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_dislay = ('id', 'title', 'release_year', 'price', 'in_stock')
    # exclude = ('in_stock', 'price')
    fields = ('id', 'title', 'genre', 'in_4k')

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

