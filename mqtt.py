#! /usr/bin/env python3
import paho.mqtt.client as mqtt

    

from db import insert_data

USER_ID = "inti2023"
URL = "broker.hivemq.com"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))






def get_date(data):
    return  data[2:10]



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = msg.payload.decode('utf-8')
    print(msg.topic+" "+ data )
    json = {}
    json["data"]=data

    if(msg.topic == "CMD"):
      elements = data.split("\n")
      for e in elements:
        date = get_date(data)
        print(f"date es {date}")
  #  insert_data(json)






client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(URL,1883,60)


class Connection():
    topics_sub = ["STATE","CMD","OPT"]
    
    
    def __init__(self,user_id = USER_ID,url = URL,sub_topic = None ) -> None:
        self.id = user_id
        self.url = url
        for topic in self.topics_sub:
            client.subscribe(topic)


    def config(self,user_id=None, url = None):
        if user_id:
            self.user_id = user_id
        if url:
            self.url = url
        



    def connection(self):
       
            client.connect(self.url,1883,60)


    def loop(self):
        client.loop_forever()





