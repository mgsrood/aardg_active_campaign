import pandas as pd

# Import lists
prospects_df = pd.read_csv('Prospects.csv')
customers_df = pd.read_csv('Customers.csv')
subscribers_df = pd.read_csv('Subscribers.csv')

print(prospects_df['Email'])

# Create email lists
prospects_emails = set(prospects_df['Email'])
customers_emails = set(customers_df['Email'])
subscribers_emails = set(subscribers_df['Email'])

# Find emails that occur in both lists
prospects_in_customers = prospects_emails.intersection(customers_emails)
prospects_in_subscribers = prospects_emails.intersection(subscribers_emails)
customers_in_subscribers = customers_emails.intersection(subscribers_emails)

print("Emails in zowel Prospects als Customers:", prospects_in_customers)
print("Emails in zowel Prospects als Subscribers:", prospects_in_subscribers)
print("Emails in zowel Customers als Subscribers:", customers_in_subscribers)