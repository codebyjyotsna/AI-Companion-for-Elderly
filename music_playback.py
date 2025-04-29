import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
SPOTIFY_CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_SPOTIFY_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

# Authenticate with Spotify
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-playback-state,user-modify-playback-state"
))

def play_music(emotion):
    """
    Play a Spotify playlist based on the detected emotion.
    """
    playlists = {
        "happy": "spotify:playlist:37i9dQZF1DXdPec7aLTmlC",  # Replace with your playlist ID
        "sad": "spotify:playlist:37i9dQZF1DX3rxVfibe1L0",
        "relaxed": "spotify:playlist:37i9dQZF1DX4WYpdgoIcn6",
    }
    playlist_uri = playlists.get(emotion, playlists["relaxed"])
    devices = spotify.devices()
    if devices["devices"]:
        spotify.start_playback(device_id=devices["devices"][0]["id"], context_uri=playlist_uri)
    else:
        print("No active Spotify devices found.")

# Example usage
detected_emotion = "happy"  # Replace with emotion detection output
play_music(detected_emotion)
