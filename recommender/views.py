from django.shortcuts import render
from .utils import get_recommendations

def index(request):
    recommended_movies = None
    if request.method == "POST":
        features = [
            int(request.POST.get('year', 2010)),
            float(request.POST.get('rating', 8.0)),
            int(request.POST.get('happy', 5)),
            int(request.POST.get('action', 5)),
            int(request.POST.get('weird', 5)),
        ]
        recommended_movies = get_recommendations(features)

    return render(request, 'index.html', {'movies': recommended_movies})