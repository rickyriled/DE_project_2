import fbchat
import time
from fbchat import Client
from fbchat.models import *

from time import sleep
from json import dumps
from kafka import KafkaProducer

thread_id = "---------------"
thread_type = ThreadType.USER
topic = 'test_topic'

#this file 'email_and_password.json' is not included in the repo of course,
#it's just a json file where the key is the account email and the value is the account password 
login_info=json.load(open('email_and_password.json'))
EMAIL=list(login_info.keys())[0]
PASSWORD=list(login_info.values())[0]

client = Client(EMAIL, PASSWORD)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


tmts_old='0'
i=0

while client.isLoggedIn():
    time.sleep(2)
    tm=client.fetchThreadMessages(thread_id=thread_id, limit=1)[0]
    tmts=tm.timestamp
    tmtx=tm.text
    
    if tmts != tmts_old:
        data = { tmts : tmtx }
        producer.send(topic, value=data)
        print("producing "+tmtx+", at "+tmts)
        tmts_old=tmts