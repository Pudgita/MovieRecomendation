from django.contrib import admin
from .models import Movie  # Импортируем твою модель

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # Эти столбцы будут видны в списке всех фильмов
    list_display = ('title', 'year', 'rating', 'happy', 'action', 'weird')