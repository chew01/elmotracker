import json


def load_translations(file_path):
    lang = {}
    with open(file_path) as lang_data_file:
        for translation in json.load(lang_data_file)["Data"]:
            if "Content" in translation:
                lang[translation["Id"]] = translation["Content"]
    return lang
