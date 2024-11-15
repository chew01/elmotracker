import re

from config import LOGFILE_PATH


def extract_token_and_uid():
    token_regex = re.compile(r'"xindong_uid":(\d+).+"access_token":"(.+?)"')
    with open(LOGFILE_PATH, encoding="utf-8") as f:
        matches = re.findall(token_regex, f.read())

    if not matches:
        return None, None

    return matches[-1]
