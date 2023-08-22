#! /usr/bin/env python3
import paho.mqtt.client as mqtt

USER_ID = "inti2023"
URL = "broker.hivemq.com"


TOPIC_STATE = "STATE"
TOPIC_DATA = "CMD"
TOPIC_OPT   ="OPT"








# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = msg.payload.decode('utf-8')
    print(msg.topic+" "+ data )





client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(URL,1883,60)


class Connection():
    topics_sub = [
        TOPIC_STATE,
        TOPIC_DATA,
        TOPIC_OPT
    ]
    
    
    def __init__(self,user_id = USER_ID,url = URL,sub_topic = None ) -> None:
       
        for topic in self.topics_sub:
            print(f"sub a"{topic})
            client.subscribe(topic)


  


    def loop(self):
        client.loop_forever()





