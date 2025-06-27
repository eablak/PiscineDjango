import requests
import json
import dewiki
import sys

def send_request(page):
    
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "parse",
        "page": page,
        "redirects": True,
        "format": "json",
        "prop": "wikitext"
    }
    
    try:
        res = requests.get(url=URL, params=PARAMS)
    except requests.HTTPError as e:
        raise e
    try:
        data = json.loads(res.text)
    except json.decoder.JSONDecodeError as e:
        raise e
    if "error" in data:
        raise Exception(data["error"]["info"])
    return(dewiki.from_string(data["parse"]["wikitext"]["*"]))
    
    


def main():

    if len(sys.argv) == 2:
        try:
            data = send_request(sys.argv[1])
        except Exception as e:
            return print(e)
        try:
            f = open("{}.wiki".format(sys.argv[1]),"w")
            f.write(data)
            f.close
        except Exception as e:
            return print(e)
    else:
        print("Error: Only one arg for page name")


if __name__ == "__main__":
    main()