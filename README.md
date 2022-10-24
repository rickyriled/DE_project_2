# Data Engineering Project #1 : Fitpipe, a hourly max heart rate ETL pipeline 
My first attempt at streaming ETL jobs; technologies include Kafka, GCS, Docker, and terraform

![alt text](image here)
## Architecture
**Container** Docker is used to set up a working version of kafka <br><br>
**Infrastructure:** Terraform is used for 'infrastructure as code' to set up a data lake in GCS<br><br>
**Streaming** Kafka producers/consumers is used in order to load streaming data from facebook chats into python for transforms and loading into GCS

**Stream flow:** The following process is run continuously through python/kafka
1. *Facebook Bots* A facebook bot scans a sets of preset chats between me and friends continously for messages, through the unoffical fbchat API
2. *Kafka Producers* The bot/chat pairs are tied to different producers and and topics in kafka
3. *Kafka Consumers* 3 consumers subscribe to the various chat topics, and filter/transform the data for user, word usage, and time series data respectively 
4. *Consumer to GCS* after performing the needed transforms, the respective consumers load the new data into tables in GCS: usr_msg_table, word_table, time_table
5. *Google Data Studio* The data upload to GCS is tied to a dashboard in google data studio, which updates every minute 


## Dashboard:
The dashboard was built using google datastudio.!!!!!!ADD DESCRIPTION!!!!!! HERE <br>
![alt text]()

## Requierments:
I was able to install most of the requierments through guides in the data engineering zoomcamp course, or through online articles. Thanks to everyone who helped with their public repos/ articles!
1. **Docker/Terraform/GCP Cloud Platform:** [DE zoomcamp guide](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp)
2. **Kafka/Kafka Docker Image** [DE zoomcamp guide](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_6_stream_processing)
4. **fbchat API:** [ Docs](https://fbchat.readthedocs.io/en/stable/)<br>
      - note, theres some common errors in setting this up; follow this github issue post: https://github.com/fbchat-dev/fbchat/issues/615

 
 ## How to run:
 Scanning Bot/ fbchat API:
  . make a new facebook account to use as a bot account; DO NOT USE YOUR OWN! it's likely this account will be banned by FB at some point
  2. Add the bot account email/password to the `email_and_password.json` file
  3. install the API through the guide in the 'requierments' section. 
  4. test if the login process works in a random python script/ jupyter notebook; if you run into errors, follow the mentioned github issue post

 Docker/Kafka:<br>
  5. set up/ install docker by following the guides in the DE zoomcamp github/ youtube lectures<br>
  6. download the kafka yaml file from DE zoomcamp week 6, use `docker-compose up` to build the kafka image/start the container<br>
  7. confirm the kafka cluster is up by opening your browser to `localhost:9021`<br>
  8. install the requierments in the requierments.txt file<br>
<br>
 
 GCS through Terraform:<br>
  9. follow the steps in the DE zoomcamp guide to set up your GCS account, envrionment varaibles and project name<br>
  10. add your gcs project name to the `passcode.sh` file<br>
  11. build the infrastrcture GCS data lake `bash tf_make_bash.sh` ; note this pulls a code listed in my git-ignore file.<br>
    - later when you want to take down your gcs bucket, use  `bash tf_destroy_bash.sh<br>
 
 Kafka Producers/Consumers:<br>
  12. run all three producer and all three consumer python scripts in the background on your computer; kafka will auto-setup the topics.<br>
    - check in your GCS bucket if the csv files are there; if so, everything is working!

