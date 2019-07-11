from boltiot import Bolt
import json, time
from twilio.rest import Client

garbage_full_limit = 5

API_KEY = "enter the one you get from the bolt dashboard>api"
DEVICE_ID  = "enter the one you get from the bolt dashboard beside your device"

account_sid = 'in your twilio account'
auth_token = 'in your twilio account'
client = Client(account_sid, auth_token)

mybolt = Bolt(API_KEY, DEVICE_ID)
response = mybolt.serialRead('10')
print (response)

while True:
    response = mybolt.serialRead('10')  #Fetching the value from Arduino
    data = json.loads(response)
    print(data)
    garbage_value = data['value'].rstrip()
    print ("Garbage level is", garbage_value)
    if (int(garbage_value) < garbage_full_limit):
        message = client.messages.create(
                              body='Sewer no. 1 is going to get clogged soon!',
                              from_='whatsapp:+from_sandbox_of_twilio_whatsapp api',
                              to='whatsapp:+your_number or the one to whom you want to send'
                          )
        print("sent")
    time.sleep(10)




