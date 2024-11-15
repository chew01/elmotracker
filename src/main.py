from datetime import datetime
from api import fetch_records
from lang import load_translations
from parser import load_items


def main():
    uid, token = input("Paste your token here!\n").split("@")
    if not uid or not token:
        print("Error: Could not retrieve UID and token.")
        return

    # Fetch records
    print("Fetching records now!")
    records = fetch_records(uid, token)
    records.reverse()

    # Load translations
    lang = load_translations("data/LangPackageTableEnusData.json")

    # Load items
    items = load_items(lang, "data/GunData.json", "data/GunWeaponData.json")

    # Print records
    for record in records:
        item = items.get(record["item"])
        timestamp = datetime.fromtimestamp(record["time"]).strftime("%Y-%m-%d %H:%M:%S")
        if item:
            print(f"{item} at {timestamp}")

    print(f"Total number of records: {len(records)}")


if __name__ == "__main__":
    main()
