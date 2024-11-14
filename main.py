from pathlib import Path
import re
import requests

ENDPOINT = 'https://gf2-gacha-record-asia.haoplay.com/list'
user_home = Path.home()
logfile_path = user_home / 'AppData/LocalLow/SunBorn/EXILIUM/Player.log'

token_regex = re.compile(r'"xindong_uid":(\d+).+"access_token":"(.+?)"')
with open(logfile_path, encoding='utf-8') as f:
    matches = re.findall(token_regex, f.read())

if not matches:
    exit(1)

uid, token = matches[-1]

results = []

headers = {'Authorization': token, 'Content-Type': 'application/x-www-form-urlencoded'}
params = {'game_channel_id': 10001, 'type_id': 3, 'u': uid}
next_req = ''
data = 'type_id=1'

while True:
    resp = requests.post(ENDPOINT, headers=headers, params=params, data=f"{next_req}{data}")
    json = resp.json()
    for record in json['data']['list']:
        results.append(record)

    next_req = f"next={json['data']['next']}&" if json['data']['next'] else ''

    if not next_req:
        break

print(len(results))