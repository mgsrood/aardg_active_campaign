import requests
import json
from dotenv import load_dotenv
import os

# Load the variables from the .env file
load_dotenv()

# ActiveCampaign parameters
api_url = os.getenv("ACTIVE_CAMPAIGN_API_URL")
api_key = os.getenv("ACTIVE_CAMPAIGN_API_KEY")

def unsubscribe_contact_by_email(email, list_id):
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
    
    # Get the contact list ID
    contact_list_response = requests.get(f'{api_url}/api/3/contactLists?contact={contact_id}&list={list_id}', headers=headers)
    if contact_list_response.status_code == 200:
        contact_list_data = contact_list_response.json()
        if contact_list_data['contactLists']:
            contact_list_id = contact_list_data['contactLists'][0]['id']
        else:
            print("Contactlijst niet gevonden.")
            return
    else:
        print(f"Error: {contact_list_response.status_code} - {contact_list_response.text}")
        return
    
    # Unsubscribe contact from list
    unsubscribe_url = f'{api_url}/api/3/contactLists/{contact_list_id}'
    unsubscribe_response = requests.delete(unsubscribe_url, headers=headers)
    
    if unsubscribe_response.status_code == 200:
        print("Contact succesvol uitgeschreven van de lijst.")
    else:
        print(f"Error: {unsubscribe_response.status_code} - {unsubscribe_response.text}")

if __name__ == "__main__":
    # Example usage
    email = 'elsdeen@gmail.com'
    list_id = 39  # Customers
    unsubscribe_contact_by_email(email, list_id)
