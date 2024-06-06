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

def get_contact_by_email(email):
    headers = {
        'Api-Token': api_key
    }
    response = requests.get(f'{api_url}/api/3/contacts?email={email}', headers=headers)
    
    if response.status_code == 200:
        contacts_data = response.json()
        contacts = contacts_data.get('contacts', [])
        if contacts:
            return contacts[0]  # Return the first contact found
        else:
            print("Geen contacten gevonden met dit e-mailadres.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

def get_tags_for_contact(contact_id):
    headers = {
        'Api-Token': api_key
    }
    response = requests.get(f'{api_url}/api/3/contacts/{contact_id}/contactTags', headers=headers)
    
    if response.status_code == 200:
        tags_data = response.json()
        return tags_data.get('contactTags', [])
    else:
        print(f"Error: {response.status_code}")
        return []

def remove_tag_from_contact(contact_tag_id):
    headers = {
        'Api-Token': api_key,
        'Content-Type': 'application/json'
    }
    response = requests.delete(f'{api_url}/api/3/contactTags/{contact_tag_id}', headers=headers)
    
    return response.status_code == 200

# Main logic
email = input("Voer het e-mailadres in: ")
tag_id_to_remove = int(input("Voer de tag ID in die je wilt verwijderen: "))

contact = get_contact_by_email(email)

if contact:
    print(f"Contact gevonden: {contact['email']}")
    tags = get_tags_for_contact(contact['id'])
    
    if tags:
        print(f"Gevonden tags: {[tag['tag'] for tag in tags]}")
        
        # Controleer of de tag ID overeenkomt met de opgegeven tag ID
        tags_to_remove = [tag for tag in tags if int(tag['tag']) == tag_id_to_remove]
        
        if tags_to_remove:
            with tqdm(total=len(tags_to_remove), desc="Removing tags", unit="tag") as pbar:
                for tag in tags_to_remove:
                    if remove_tag_from_contact(tag['id']):
                        pbar.update(1)
                    else:
                        print(f"Error removing tag ID {tag['id']}")
            print(f"Tag ID {tag_id_to_remove} verwijderd voor contact {email}")
        else:
            print(f"Tag ID {tag_id_to_remove} niet gevonden voor contact {email}")
    else:
        print(f"Geen tags gevonden voor contact {email}")
else:
    print("Geen contact gevonden met dit e-mailadres.")
