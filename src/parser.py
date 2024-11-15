import json
from item import Gun, Weapon


def load_items(lang, gun_data_path, weapon_data_path):
    items = {}

    with open(gun_data_path) as gun_data_file, open(
        weapon_data_path
    ) as weapon_data_file:
        gun_data = json.load(gun_data_file)["Data"]
        weapon_data = json.load(weapon_data_file)["Data"]

        for gun in gun_data:
            items[gun["Id"]] = Gun(lang[gun["Name"]["Id"]], gun["Rank"])
        for weapon in weapon_data:
            items[weapon["Id"]] = Weapon(lang[weapon["Name"]["Id"]], weapon["Rank"])

    return items
