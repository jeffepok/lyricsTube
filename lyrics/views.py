from django.shortcuts import render
from .models import Song
# Create your views here.
def index(request):
    return render(request, "lyrics/index.html", {
        "song":  Song.objects.all()
    }
    )