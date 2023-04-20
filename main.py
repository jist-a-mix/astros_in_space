import requests
import json
def req(url):
    response = requests.get(url)
    print(response.status_code)
    jprint(response.json()
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

if __name__ == '__main__':
    req('http://api.open-notify.org/astros.json')


