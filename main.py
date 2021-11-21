from base64 import encode
from flask import Flask
from flask import render_template, redirect, request, jsonify
from musixmatch import Musixmatch
import requests
import base64
import logging
import json
import random

redirect_uri = "http://169.234.34.232:6378/callback"
app = Flask(__name__)
musixmatch = Musixmatch('777aba81aa95a4b792db0907518ccdb3')
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
   return render_template("index.html")


@app.route("/login")
def request_user_auth():
  """Request authorization from user."""
  
  client_id = "18b9a065ebd24e1da5764b78fffcdc0b"
  
  login_url = f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&scope=user-top-read&redirect_uri={redirect_uri}"
  return redirect(login_url)


@app.route("/callback")
def callback():
  """Recieve access token from Spotify."""
  client_id = "18b9a065ebd24e1da5764b78fffcdc0b" 

  code = str(request.query_string)
  code = code.split("=")
  code = code[-1][:-1]

  encoded_auth = f"{client_id}:40e9eaa84ab843b6bc558ec21ad51535"
  encoded_auth = encoded_auth.encode("ascii")
  encoded_auth = base64.urlsafe_b64encode(encoded_auth)
  
  request_body = {"grant_type": "authorization_code", "code": code, "redirect_uri": redirect_uri, "client_id": "18b9a065ebd24e1da5764b78fffcdc0b", "client_secret": "40e9eaa84ab843b6bc558ec21ad51535",}
  posted = requests.post(url="https://accounts.spotify.com/api/token", data=request_body, headers={"Content-Type": "application/x-www-form-urlencoded"})
  token = posted.json()['access_token']
  
  user_top_request = requests.get(url="https://api.spotify.com/v1/me/top/tracks/?limit=50", headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"})
  user_top = user_top_request.json()
  app.logger.info("Data obtained")
  top_songs = []

  for song in user_top["items"]:
    song_name = song["name"]
    artist = song["artists"][0]["name"]
    if len(song_name) == 0 or len(artist) == 0:
      continue
    else:
      top_songs.append([song_name, artist])
  app.logger.info("Found Top Songs")
  snippets = []
  for i in top_songs:
    curr_track = i[0] + ", " + i[1]
    song = i[0]
    artist = i[1]
    info = musixmatch.matcher_track_get(song, artist)
    app.logger.info(info)
    if info['message']['header']['status_code'] != 200 or info['message']['body']['track']['has_lyrics'] != 1:
      print("Failed")
      continue
    else:
      id = info['message']['body']['track']['track_id']
      snippet = musixmatch.track_snippet_get(id)['message']['body']['snippet']['snippet_body']
      if snippet == "":
        continue
      else:
        snippets.append([snippet, curr_track])
  app.logger.info('Found Snippets')
  return render_template("quiz.html",snippets=json.dumps(snippets))


if __name__ == "__main__":
  """  app.run(
      host = '0.0.0.0',
      port = '6378',
      debug = "True"
    )
  """

  app.run(
      host='0.0.0.0',
      port=random.randint(2000, 9000),
      debug = "True"
    )