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
    except:
        raise requests.HTTPError
    try:
        data = json.loads(res.text)
    except:
        raise json.decoder.JSONDecodeError
    if data.get("error") is not None:
        raise Exception(data["error"]["info"])
    return(dewiki.from_string(data["parse"]["wikitext"]["*"]))



if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        try:
            data = send_request(sys.argv[1])
        except Exception as e:
            raise e
        try:
            f = open("{}.wiki".format(sys.argv[1]),"w")
            f.write(data)
            f.close
        except Exception as e:
            raise e
    else:
        print("Error: Only one arg for page name")