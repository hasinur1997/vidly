from django.urls import path
from . import   views

app_root_name = ''

urlpatterns = [
    path('', views.index, name="movie_index"),
    path('<int:movie_id>', views.detail, name="movie_detail"),
]
