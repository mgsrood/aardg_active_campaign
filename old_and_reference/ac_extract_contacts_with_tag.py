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

def get_emails_with_tag(tag_id):
    headers = {
        'Api-Token': api_key
    }
    email_list = []
    offset = 0
    limit = 100

    with tqdm(total=1, desc="Fetching contacts", unit="contacts") as pbar:
        while True:
            response = requests.get(f'{api_url}/api/3/contacts?tagid={tag_id}&limit={limit}&offset={offset}', headers=headers)
            
            if response.status_code == 200:
                contacts_data = response.json()
                contacts = contacts_data.get('contacts', [])
                if not contacts:
                    break
                emails = [contact['email'] for contact in contacts]
                email_list.extend(emails)
                offset += limit

                # Update de voortgangsbalk
                pbar.update(len(contacts))
                pbar.total = len(email_list) + limit
            else:
                print(f"Error: {response.status_code}")
                break

    return email_list

if __name__ == "__main__":
    # Extract emails with tag Klant / 74
    tag_id = 74
    emails_with_tag = get_emails_with_tag(tag_id)

    # Print outcome
    if emails_with_tag:
        print(f"Found {len(emails_with_tag)} email addresses with tag ID {tag_id}")
        print(emails_with_tag)
    else:
        print("Geen contacten gevonden met deze tag.")
