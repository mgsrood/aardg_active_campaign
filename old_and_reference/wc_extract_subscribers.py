from woocommerce import API
from dotenv import load_dotenv
import os

# Load the variables from the .env file
load_dotenv()

# WooCommerce parameters
consumer_key = os.getenv("WOOCOMMERCE_CONSUMER_KEY")
consumer_secret = os.getenv("WOOCOMMERCE_CONSUMER_SECRET")
url = os.getenv("WOOCOMMERCE_URL")

# Configuring the WooCommerce API
wcapi = API(
    url=url,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    wp_api=True,
    version="wc/v3",
    timeout=30  # Increase the timeout to 30 seconds
)

def fetch_subscription_emails_by_status(status):
    # Initialize list to hold email addresses
    email_list = []

    # Pagination
    page = 1
    while True:
        print(f"Fetching page {page}...")
        subscription_response = wcapi.get(f"subscriptions", params={"status": status, "page": page, "per_page": 100})
        subscriptions = subscription_response.json()
        
        if not subscriptions:
            break
        
        for subscription in subscriptions:
            customer_id = subscription['customer_id']
            customer_response = wcapi.get(f"customers/{customer_id}")
            customer = customer_response.json()
            email_list.append(customer['email'])
        
        page += 1

    return email_list

if __name__ == "__main__":
    # Example usage
    status = 'active'  # or 'on-hold'
    email_list = fetch_subscription_emails_by_status(status)
    print(email_list)
