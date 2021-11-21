from flask import Flask, render_template, redirect, request
from musixmatch import Musixmatch
import requests
import base64

app = Flask(__name__)
musixmatch = Musixmatch('777aba81aa95a4b792db0907518ccdb3')

def get_snippets(songs: list[list[str]], limit: int) -> list[list[str]]:
  try:
    songs = callback()
  except:
    raise Exception('Could not retrieve data')
  snippets = []
  num_found = 0
  for i in songs:
    curr_track = i[0] + ", " + i[1]
    song = i[0]
    artist = i[1]
    info = musixmatch.matcher_track_get(song, artist)
    if info['header']['status_code'] != 200 or info['message']['body']['has_lyrics'] != 1:
      print("Failed")
      continue
    else:
      id = info['message']['body']['track']['track_id']
      snippet = musixmatch.track_snippet_get(id)['message']['body']['snippet']['snippet_body']
      if snippet == "":
        continue
      else:
        snippets.append((snippet, curr_track))
        num_found += 1
      if num_found == limit:
        return snippets
  return snippets


@app.route("/")
def index():
   return render_template("index.html")


@app.route("/login")
def request_user_auth():
  """Request authorization from user."""
  
  client_id = "18b9a065ebd24e1da5764b78fffcdc0b"
  redirect_uri = "http://169.234.55.163:6378/callback" 
  
  login_url = f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&scope=user-top-read&redirect_uri={redirect_uri}"
  return redirect(login_url)


@app.route("/callback")
def callback():
  """Recieve access token from Spotify."""
  client_id = "18b9a065ebd24e1da5764b78fffcdc0b" 
  redirect_uri = "http://169.234.55.163:6378/callback"

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
  
  top_songs = []

  for song in user_top["items"]:
    song_name = song["name"]
    artist = song["artists"][0]["name"]
    if len(song_name) == 0 or len(artist) == 0:
      continue
    else:
      top_songs.append([song_name, artist])
  return str(top_songs)


if __name__ == "__main__":
  app.run(
    host = '0.0.0.0',
    port = '8080',
    debug = "True"
  )