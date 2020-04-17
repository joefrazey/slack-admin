import requests, csv, json, time, pandas as pd
from datetime import date

today = date.today()

today = today.strftime("%b %d %Y")

## ENTER TOKEN FOR WORKSPACE IN WHICH CHANNEL RESIDES IN

TOKEN = ""

CURSOR = ""

## ENTER CHANNEL ID OF CHANNEL YOU WISH TO EXTRACT MEMBERS FROM
CHANNEL = ""

PARAMS = {
    "token": TOKEN,
    "channel": CHANNEL,
    "cursor": "",
    "limit": 1000
}

target_users = []


while True:
        PARAMS['cursor'] = CURSOR
        r = requests.get("https://slack.com/api/conversations.members", params = PARAMS)
        if r.status_code == 200:
            data = r.json()
            if data['ok']:                
                if data['response_metadata']['next_cursor'] == "":
                    for user in data['members']:
                        target_users.append(user)
                    print("Done processing all channels")
                    break
                else:
                    CURSOR = data['response_metadata']['next_cursor']
                    for user in data['members']:
                        target_users.append(user)

## Above will give you User IDs

export = ## download an export from [workspace_name].slack.com/stats#members

## Will isolate the users in the channel
channelUsers = export[export['User ID'].isin(target_users)]

## from here you can use these emails/IDs however you wish