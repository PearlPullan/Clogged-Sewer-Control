from boltiot import Bolt
import json, time
from twilio.rest import Client

garbage_full_limit = 5

API_KEY = "7913e4ae-fa53-42c2-b4a7-d72efe7d0283"
DEVICE_ID  = "BOLT3635841"

account_sid = 'ACc49c9423be6720aa90c946580b7895e8'
auth_token = '8be2d242cfec455552ca5d91bd546973'
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
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919711488349'
                          )
        print("sent")
    time.sleep(10)




