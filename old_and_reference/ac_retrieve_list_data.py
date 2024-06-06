import requests
import json
from dotenv import load_dotenv
import os

# Load the variables from the .env file
load_dotenv()

# ActiveCampaign parameters
api_url = os.getenv("ACTIVE_CAMPAIGN_API_URL")
api_key = os.getenv("ACTIVE_CAMPAIGN_API_KEY")

def get_all_lists():
    headers = {
        'Api-Token': api_key
    }
    lists_list = []
    offset = 0
    limit = 100 

    while True:
        response = requests.get(f'{api_url}/api/3/lists?limit={limit}&offset={offset}', headers=headers)
        
        if response.status_code == 200:
            lists_data = response.json()
            lists = lists_data.get('lists', [])
            if not lists:
                break
            lists_list.extend(lists)
            offset += limit
        else:
            print(f"Error: {response.status_code}")
            break

    return lists_list

# Haal alle lijst data op
lists_data = get_all_lists()

if lists_data:
    lists_list = [{'id': lst['id'], 'name': lst['name']} for lst in lists_data]
    print(json.dumps(lists_list, indent=4))
else:
    print("Geen lijsten gevonden of een fout opgetreden.")
