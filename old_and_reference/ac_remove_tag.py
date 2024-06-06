import requests
import json
from dotenv import load_dotenv
import os

# Load the variables from the .env file
load_dotenv()

# ActiveCampaign parameters
api_url = os.getenv("ACTIVE_CAMPAIGN_API_URL")
api_key = os.getenv("ACTIVE_CAMPAIGN_API_KEY")

def remove_tag_from_contact_by_email(email, tag_id):
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
    
    # Remove tag from contact
    url = f'{api_url}/api/3/contacts/{contact_id}/contactTags'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        contact_tags = response.json().get('contactTags', [])
        for contact_tag in contact_tags:
            if contact_tag['tag'] == str(tag_id):
                contact_tag_id = contact_tag['id']
                delete_url = f'{api_url}/api/3/contactTags/{contact_tag_id}'
                delete_response = requests.delete(delete_url, headers=headers)
                
                if delete_response.status_code == 200:
                    print("Tag succesvol verwijderd van contact.")
                else:
                    print(f"Error: {delete_response.status_code} - {delete_response.text}")
                return
        print("Tag niet gevonden voor dit contact.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Example usage
    email = 'aadwent@orange.fr'
    tag_id = 832  
    
    remove_tag_from_contact_by_email(email, tag_id)