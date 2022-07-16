import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_recommendations():
  songs = []
  artists = []
  main = []
  search = "Take me to church"
  sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials('fc0eea0cf28c49648e3820786ceaa963','5bb611de39e44c41bfa7ed7fcccb0eb3'))
  result = sp.search(q=search,limit=1)
  id_list=[result['tracks']['items'][0]['id']]
  recommendations=sp.recommendations(seed_tracks=id_list,limit=100)
  for i in range(len(recommendations["tracks"])):
    songs.append(recommendations["tracks"][i]["album"]["name"])
  for i in range(len(recommendations["tracks"])):
    artists.append(recommendations["tracks"][i]["album"]["artists"][0]["name"])
  main.append(songs)
  main.append(artists)
  return main

main = get_recommendations()
print(main)
