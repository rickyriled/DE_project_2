from kafka import KafkaConsumer
from json import loads
from time import sleep
from google.cloud import storage
import json
import os
import sys
import pandas as pd

CSV_NAME='user_msg_table.csv'
BUCKET_NAME='kafka_buck'
topic = ['chat_one', 'chat_two', 'chat_three']

PATH=os.environ['GOOGLE_APPLICATION_CREDENTIALS']
storage_client = storage.Client(PATH)
bucket=storage_client.get_bucket(BUCKET_NAME)

consumer = KafkaConsumer(
    topic,
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='user_id',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


while(True):
    print("inside while", end="...")

    for message in consumer:
        #read in current data frame state
        df1=pd.read_csv(CSV_NAME)
        
        #display value to add
        print(message.value, end="...")

        #produce data entry
        print('produce',end="....")
        datalist= list(message.value.values())[0]
  
        user_ID = datalist[1]
        msg_len = len(datalist[2].split(" "))

        data={'user_id':[user_ID], 'count' : [1], 'msg_len' : [msg_len]}
        df2=pd.DataFrame(data)

        #append and write update
        print('write',end="....")
        df3=df1.append(df2)
        df3.to_csv(CSV_NAME, index=False)

        #push update to the cloud
        print('push',end="....")
        UPLOADFILE = os.path.join(os.getcwd(),CSV_NAME)
        blob=bucket.blob(CSV_NAME)
        blob.upload_from_filename(UPLOADFILE)
        
        print('sucess!')
        #wait
        sleep(2)