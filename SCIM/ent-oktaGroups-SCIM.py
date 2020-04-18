## This code will show you all of your okta groups for your enterprise

import requests, json, csv
import pandas as pd

TOKEN = ## NEED SCIM TOKEN
headers = {
    "Authorization": f"Bearer {TOKEN}"
}
index = 1
COUNT = 1000


base_url = f"https://api.slack.com/scim/v1/Groups?count={COUNT}"
result = []

n = 0

while True:
    print(f"Getting page with index = {index}")
    r = requests.get(f"{base_url}&startIndex={index}", headers = headers)
    if r.status_code == 200:
        data = r.json()
        itemsOnPage = data['itemsPerPage']
        totalResults = data['totalResults']
        for resource in data['Resources']:
            group_id = resource.get('id')
            group_name = resource.get('displayName')
            group_url = data['Resources'][n]['meta']['location']
            n = n + 1
            result.append([group_name, group_id, group_url])
            # print(f"{group_name}\t\t{group_id}")
        
        # Pagination support
        if index + itemsOnPage >= totalResults:
            break
        else:
            index = index + itemsOnPage

df = pd.DataFrame(result, columns = ["Group Name", "Group ID", "Group URL"])