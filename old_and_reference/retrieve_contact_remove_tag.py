import requests
import json
from tqdm import tqdm
from old_and_reference.ac_extract_contacts_with_tag import get_emails_with_tag
from ac_remove_tag import remove_tag_from_contact_by_email
from dotenv import load_dotenv
import os

# Vriendenkorting-verzender tag
tag_id = 55 

# Load the variables from the .env file
load_dotenv()

# ActiveCampaign parameters
api_url = os.getenv("ACTIVE_CAMPAIGN_API_URL")
api_key = os.getenv("ACTIVE_CAMPAIGN_API_KEY")

# Extract emails with specific tag
emails_with_tag = get_emails_with_tag(tag_id)

# Remove the specific tag from the contacts with those tags
for mail in emails_with_tag:
    remove_tag_from_contact_by_email(mail, tag_id)
