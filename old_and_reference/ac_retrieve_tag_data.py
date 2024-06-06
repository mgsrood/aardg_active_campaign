import requests
import json
from dotenv import load_dotenv
import os

# Load the variables from the .env file
load_dotenv()

# ActiveCampaign parameters
api_url = os.getenv("ACTIVE_CAMPAIGN_API_URL")
api_key = os.getenv("ACTIVE_CAMPAIGN_API_KEY")

def get_all_tags():
    headers = {
        'Api-Token': api_key
    }
    tags_list = []
    offset = 0
    limit = 100 

    while True:
        response = requests.get(f'{api_url}/api/3/tags?limit={limit}&offset={offset}', headers=headers)
        
        if response.status_code == 200:
            tags_data = response.json()
            tags = tags_data.get('tags', [])
            if not tags:
                break
            tags_list.extend(tags)
            offset += limit
        else:
            print(f"Error: {response.status_code}")
            break

    return tags_list

# Haal alle tag data op
tags_data = get_all_tags()

if tags_data:
    tags_list = [{'id': tag['id'], 'name': tag['tag']} for tag in tags_data]
    print(json.dumps(tags_list, indent=4))
else:
    print("Geen tags gevonden of een fout opgetreden.")
