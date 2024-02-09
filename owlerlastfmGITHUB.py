import requests
import json
from base64 import b64encode


r = requests.get("http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=LASTFMUSERNAME&api_key=LASTFMAPIKEYHERE&format=json")
response_json = json.loads(r.text)
if '@attr' in response_json['recenttracks']['track'][0]:
    recent_track = response_json['recenttracks']['track'][0]

    nowplaying = recent_track ['@attr']['nowplaying']
    artist = recent_track['artist']['#text']
    name = recent_track['name']
    print('I am listening to', name, 'by',  artist,'...','nifty...')


    username = "INPUTUSERNAMEHERE"
    password = "INPUTPASSWORDHERE"
    requests.get("https://api.owler.cloud/v1/account/verify_credentials.json", auth=(username, password))
    url = "https://api.owler.cloud/v1/statuses/update.json"
    requests.post(f"{url}?status=I'm listening to {name} by {artist}.", auth=(username, password))
    print("Success! Check the public timeline.")

