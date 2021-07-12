from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import Movies


# Create your views here.
def index(request):
    movies = Movies.objects.all()
    return render(request, "movies/index.html", {"movies": movies})


def detail(request, movie_id):
    try:
        movie = Movies.objects.get(id=movie_id)
        return render(request, 'movies/detail.html', {"movie": movie})
    except Movies.DoesNotExist:
        raise Http404()
