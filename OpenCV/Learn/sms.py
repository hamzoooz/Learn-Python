from __future__ import print_function
from telesign.messaging import MessagingClient

customer_id = input('Enter your customer id>>: ')
api_key =input('Enter your api>:')

phone_number =input('Enter your phone number>>:')
message = "hello am mohmad"
message_type = "ARN"

messaging = MessagingClient(customer_id, api_key)
response = messaging.message(phone_number, message, message_type)

    

print("ok mohmad")


