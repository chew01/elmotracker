import requests
from config import ENDPOINT


def fetch_records(uid, token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    params = {"game_channel_id": 10001, "type_id": 3, "u": uid}
    next_req = ""
    data = "type_id=1"
    results = []

    while True:
        resp = requests.post(
            ENDPOINT, headers=headers, params=params, data=f"{next_req}{data}"
        )
        resp_json = resp.json()

        results.extend(resp_json["data"]["list"])

        next_req = (
            f"next={resp_json['data']['next']}&" if resp_json["data"]["next"] else ""
        )

        if not next_req:
            break

    return results
