import spotipy

scopes = 'user-follow-read user-follow-modify playlist-read-collaborative playlist-read-private playlist-modify-public playlist-modify-private'

def main():
    spotify = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope=scopes, redirect_uri="http://localhost:8080"))
    tokyo = spotify.artist('5TbLOwv8BNnik3f03NZJlt') # Get artist page
    tokyo_albums = spotify.artist_albums(tokyo['id']) # Get albums from artist page (uses ID)
    tokyo_songs = [] # Make an empty list of songs
    for album in tokyo_albums['items']: # Scan every album discovered on line 8 as "album"
        for track in spotify.album_tracks(album['id'])['items']: # Scan every track discovered on line 10 as "track"
            tokyo_songs.append(track['id']) # Add the track by it's ID to the empty list on line 9

    playlists = spotify.current_user_playlists() # Get all of the users playlists
    if spotify.current_user_following_artists([tokyo['id']]): # If the user is following TOKYO'S REVENGE ...
        spotify.user_unfollow_artists([tokyo['id']]) # ... then unfollow TOKYO'S REVENGE
    
    for playlist in playlists['items']: # Scan every playlist discovered on line 14 as "playlist"
        if playlist['owner']['external_urls']['spotify'] is spotify.me()['external_urls']['spotify']: # If you are the owner of the playlist...
            spotify.user_playlist_remove_all_occurrences_of_tracks(spotify.me()['id'], 
                playlist['id'], tokyo_songs) # Remove all occurrences of a TOKYO'S REVENGE song.
            
if __name__ == "__main__":
    main()