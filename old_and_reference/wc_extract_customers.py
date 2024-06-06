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
    version="wc/v3"
)

def fetch_all_customer_emails():
    # Initialize list to hold email addresses
    email_list = []

    # Pagination
    page = 1
    while True:
        print(f"Fetching page {page}...")
        customer_response = wcapi.get(f"customers", params={"page": page, "per_page": 100})
        customers = customer_response.json()
        
        if not customers:
            break
        
        for customer in customers:
            email_list.append(customer['email'])
        
        page += 1

    return email_list

if __name__ == "__main__":
    # Fetch all customer emails
    customer_emails = fetch_all_customer_emails()
    print(customer_emails)
