import requests
import json
from tqdm import tqdm
from dotenv import load_dotenv
import os

# Load the variables from the .env file
load_dotenv()

# ActiveCampaign parameters
api_url = os.getenv("ACTIVE_CAMPAIGN_API_URL")
api_key = os.getenv("ACTIVE_CAMPAIGN_API_KEY")

def get_emails_from_list(list_id):
    headers = {
        'Api-Token': api_key
    }
    email_list = []
    offset = 0
    limit = 100

    with tqdm(total=1, desc="Fetching contacts", unit="contacts") as pbar:
        while True:
            response = requests.get(f'{api_url}/api/3/contacts?listid={list_id}&limit={limit}&offset={offset}', headers=headers)
            
            if response.status_code == 200:
                contacts_data = response.json()
                contacts = contacts_data.get('contacts', [])
                if not contacts:
                    break
                emails = [contact['email'] for contact in contacts]
                email_list.extend(emails)
                offset += len(contacts)

                # Update de voortgangsbalk
                pbar.update(len(contacts))
                pbar.total = offset + limit
            else:
                print(f"Error: {response.status_code} - {response.text}")
                break

    return email_list

if __name__ == "__main__":
    # Extract emails from list
    list_id = 39  
    emails_from_list = get_emails_from_list(list_id)

    # Print outcome
    if emails_from_list:
        print(f"Found {len(emails_from_list)} email addresses in list ID {list_id}")
    else:
        print("Geen contacten gevonden in deze lijst.")
