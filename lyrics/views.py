from django.shortcuts import render
from .models import Song
# Create your views here.
def index(request):
    return render(request, "lyrics/index.html", {
        "song":  Song.objects.all()
    }
    )
def lyrics(request, song_title):
    song = Song.objects.get(title = song_title)
    return render(request, "lyrics/lyrics.html",{
        "song": song
    })