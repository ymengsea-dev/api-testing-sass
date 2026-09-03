import shlex
import json
from app.models.enum_type import HttpMethod

def curl_parser(raw_curl: str)-> dict:
    # curl command often with trailing `\` for line continuation —
    # shlex don't care about newline, but strip the blackslashes for safety
    cleaned_curl = raw_curl.replace("\\n", " ").replace("\\r\n", "")

    tokens = shlex.split(cleaned_curl)

    method = HttpMethod.GET
    url = None
    headers = {}
    body_raw = None

    i = 0
    while i < len(tokens):

        token = tokens[i]

        if token == "curl":
            i += 1
            continue
        if token in ("-X", "--request"):
            method = tokens[i + 1].upper()
            i += 2
            continue
        if token in ("-H", "--header"):
            header_line = tokens[i + 1]
            key, _, value = header_line.partition(":")
            headers[key.strip()] = value.strip()
            i += 2
            continue
        if token in ("-d", "--data", "--data-raw", "--data-binary"):
            body_raw = tokens[i + 1]
            if method == HttpMethod.GET:
                method = HttpMethod.POST  # curl implies POST when -d is present and -X wasn't given
            i += 2
            continue
        if token.startswith("http://") or token.startswith("https://"):
            url = token
            i += 1
            continue
        i += 1
    body = None

    if body_raw:
        try:
            body = json.loads(body_raw)
        except json.JSONDecodeError:
            body = None
    
    return {
        "method": method,
        "url": url,
        "headers": headers,
        "body": body,
    }