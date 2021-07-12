from django.contrib import admin
from . models import Genre, Movies


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'number_in_stock', 'daily_rate', 'genre', )


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MovieAdmin)

