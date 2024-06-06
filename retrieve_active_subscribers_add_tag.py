from dotenv import load_dotenv
import os
from woocommerce import API
from old_and_reference.wc_extract_subscribers import fetch_subscription_emails_by_status
from old_and_reference.ac_add_tag import add_tag_to_contact_by_email

# Define the Abo-Actief tag
tag_id = 71 # Abo-Actief tag
status = 'active'

# Load the variables from the .env file
load_dotenv()

# WooCommerce parameters
consumer_key = os.getenv("WOOCOMMERCE_CONSUMER_KEY")
consumer_secret = os.getenv("WOOCOMMERCE_CONSUMER_SECRET")
url = os.getenv("WOOCOMMERCE_URL")

# ActiveCampaign parameters
api_url = os.getenv("ACTIVE_CAMPAIGN_API_URL")
api_key = os.getenv("ACTIVE_CAMPAIGN_API_KEY")

# Retrieve customer mail list
customer_email_list = fetch_subscription_emails_by_status(status)

# Add Klant tag to customers in ActiveCampaign
for mail in customer_email_list:
    add_tag_to_contact_by_email(mail, tag_id)