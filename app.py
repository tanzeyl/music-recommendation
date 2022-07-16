import numpy as np
from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_recommendations(query):
  songs = []
  artists = []
  main = []
  search = query
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

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
  return render_template('index.html')


@app.route("/search", methods=["GET", "POST"])
def result():
  if request.method == "POST":
      query = request.form.get("query")
      main = get_recommendations(query)
      return render_template('index.html', list1 = main, l = len(main[0]))

if __name__ == "__main__":
  app.run(debug=True)
