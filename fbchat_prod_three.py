import fbchat
import time
from fbchat import Client
from fbchat.models import *

from time import sleep
from json import dumps
import json as json
from kafka import KafkaProducer

from datetime import datetime

thread_id = "---------"  #Enter thread ID heere
thread_type = ThreadType.USER
topic = 'chat_three'

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

def get_data(msg):
    fb_msg=msg[0]
    
    timestamp = float(fb_msg.timestamp)/1000
    date_time = datetime.fromtimestamp(timestamp)
    
    user_id = fb_msg.author
    
    msg_txt = fb_msg.text
    
    return [str(date_time), user_id, msg_txt]

while True:
    time.sleep(2)
    message=client.fetchThreadMessages(thread_id=thread_id, limit=1)
    tm=message[0]
    tmts=tm.timestamp
    
    important_data=get_data(message)
    if tmts != tmts_old:
        data = { 'prod_1' : important_data }
        producer.send(topic, value=data)
        print("producing "+str(important_data)+", at "+tmts)
        tmts_old=tmts