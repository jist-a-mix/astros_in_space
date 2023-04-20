
import requests
import json

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def req(url):
    # Use a breakpoint in the code line below to debug your script.
    response = requests.get(url)
    print(response.status_code)
    jprint(response.json())# Press Ctrl+F8 to toggle the breakpoint.
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    req('http://api.open-notify.org/astros.json')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
