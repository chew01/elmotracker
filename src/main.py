from datetime import datetime
from api import fetch_records
from lang import load_translations
from parser import load_items
from utils import extract_token_and_uid


def main():
    uid, token = extract_token_and_uid()
    if not uid or not token:
        print("Error: Could not retrieve UID and token.")
        return

    # Fetch records
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
