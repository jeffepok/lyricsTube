import pandas as pd
from lyrics.models import Song
df = pd.read_csv("Akan Gospel Songs _ Ghospel Lyrics.csv")
df['lyrics'] = df['lyrics'].str.replace("\r\n", "")
df['lyrics'] = df['lyrics'].str.strip()
df['Title'] = df['Title'].str.replace(f"[^a-zA-Z,εƆɔ0-9. ]", "")
for index, song in df.iterrows():
    new_song = Song(title = song['Title'], lyrics = song['lyrics'])
    new_song.save()