import requests
import json
from dotenv import load_dotenv
import os

# Load the variables from the .env file
load_dotenv()

# ActiveCampaign parameters
api_url = os.getenv("ACTIVE_CAMPAIGN_API_URL")
api_key = os.getenv("ACTIVE_CAMPAIGN_API_KEY")

def add_tag_to_contact_by_email(email, tag_id):
    # Get contact by email
    headers = {
        'Api-Token': api_key
    }
    params = {
        'email': email
    }
    response = requests.get(f'{api_url}/api/3/contacts', headers=headers, params=params)
    
    if response.status_code == 200:
        contact_data = response.json()
        if contact_data['contacts']:
            contact_id = contact_data['contacts'][0]['id']
        else:
            print("Contact niet gevonden.")
            return
    else:
        print(f"Error: {response.status_code}")
        return
    
    # Add tag to contact
    url = f'{api_url}/api/3/contactTags'
    headers = {
        'Api-Token': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'contactTag': {
            'contact': contact_id,
            'tag': tag_id
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        print("Tag succesvol toegevoegd aan contact.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Example usage
    email = 'aadwent@orange.fr'
    tag_id = 832  
    
    add_tag_to_contact_by_email(email, tag_id)