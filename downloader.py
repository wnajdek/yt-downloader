from pytube import YouTube
from pytube import Playlist

def downloadVideo(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Blad dla adresu: " + link)
    print("Pobieranie zakonczone.")


def downloadPlaylist(link):
    playlist = Playlist(link)
    try:
        for video in playlist.videos:
            video.streams.first().download()
    except:
        print("Blad przy probie pobrania playlisty spod adresu: " + link)


choice = input("Jezeli chcesz pobrac playliste wpisz 'p': ")
playlistSelected = choice.lower() == "p"
txtForPrompt = "playlisty" if playlistSelected else "wideo"

link = input(f"Podaj adres URL do {txtForPrompt}: ")
if playlistSelected:
    downloadPlaylist(link)
else:
    downloadVideo(link)
