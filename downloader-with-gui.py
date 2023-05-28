import tkinter as tk
from pytube import YouTube
from pytube import Playlist

def downloadVideo(link):
    message_label.config(text="")
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Blad dla adresu: " + link)
    print("Pobieranie zakonczone.")
    message_label.config(text="Pobieranie zakończone.", fg="green")


def downloadPlaylist(link):
    message_label.config(text="")
    playlist = Playlist(link)
    try:
        for video in playlist.videos:
            video.streams.filter(only_audio=True).first().download()
        print("Pobieranie zakonczone");
        message_label.config(text="Pobieranie zakończone.", fg="green")
    except:
        print("Blad przy probie pobrania playlisty spod adresu: " + link)


def submit():
    link = entry.get()
    if link:
        print("Input value:", link)
        if var.get() == 1:
            print("Radio button selected: Wideo")
            downloadVideo(link)
        elif var.get() == 2:
            print("Radio button selected: Playlista")
            downloadPlaylist(link)
        else:
            message_label.config(text="Wybierz opcję!", fg="red")
    else:
        message_label.config(text="Wprowadź link!", fg="red")

# Create the main Tkinter window
window = tk.Tk()
window.title("Youtubowy Pobieracz")
window.minsize(300, 300)

# Create an Entry widget for input
entry = tk.Entry(window)
entry.pack()

# Create a variable to store the radio button value
var = tk.IntVar()

# Create a radio button
radio_button1 = tk.Radiobutton(window, text="Wideo", variable=var, value=1)
radio_button1.pack()

# Create another radio button
radio_button2 = tk.Radiobutton(window, text="Playlista", variable=var, value=2)
radio_button2.pack()

# Create a Submit button
submit_button = tk.Button(window, text="Pobierz", command=submit)
submit_button.pack()

# Create a label to display messages
message_label = tk.Label(window, text="")
message_label.pack()

# Start the Tkinter event loop
window.mainloop()
