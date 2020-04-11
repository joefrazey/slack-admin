import requests, csv, json


TOKEN = ## NEED TOKEN
CURSOR = ""
PARAMS = {
    "token": TOKEN,
    "cursor": "",
    "limit": 1000
}

while True:
        PARAMS['cursor'] = CURSOR
        r = requests.get("https://slack.com/api/conversations.list", params = PARAMS)
        if r.status_code == 200:
            data = r.json()
            if data['ok']:                
                if data['response_metadata']['next_cursor'] == "":
                    print("Done processing all channels")
                    break
                else:
                    CURSOR = data['response_metadata']['next_cursor']
channels = []

for name in data['channels']:
    print(name['name'])
    channels.append(name['name'])