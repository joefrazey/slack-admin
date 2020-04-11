import requests, json, csv, pandas as pd

## EDIT THESE VALUES
TOKEN = ## NEED ADMIN TOKEN


## DO NOT EDIT BELOW HERE

url = "https://api.slack.com/scim/v1//Users"
startIndex = 0
COUNT = 1000

query_params = {
    "startIndex": 0,
    "count": 1000
}
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

all_ids = []
emails = []
group = []
active = []

while True:
    r = requests.get(url, params = query_params, headers = headers)
    if r.status_code == 200:
        data = r.json()
        for userid in data['Resources']:
            all_ids.append(userid['id'])
            emails.append(userid['emails'][0]['value'])
            group.append(userid['groups'])
            active.append(userid['active'])
        if data['itemsPerPage'] < COUNT:
            break
        startIndex += data['itemsPerPage']
        query_params['startIndex'] = startIndex

ids = pd.DataFrame({'id': all_ids, 'Email': emails, 'groups': group, 'active': active})