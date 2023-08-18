import paho.mqtt.client as mqtt




USER_ID = "inti2023"
URL = "broker.hivemq.com"








# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+ msg.payload.decode('utf-8'))





client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(URL,1883,60)






class Connection():
    topics_sub = []
    
    
    def __init__(self,user_id = USER_ID,url = URL,sub_topic = None ) -> None:
        self.id = user_id
        self.url = url
        if sub_topic:
            self.sub(sub_topic)


    def config(self,user_id=None, url = None):
        if user_id:
            self.user_id = user_id
        if url:
            self.url = url
        

    def sub(self,topic):
        print(f"sub to {topic}")
        self.topics_sub += topic
        client.subscribe(topic)


    def connection(self,url = None):
        if url:
            client.connect(url, 1883, 60)
        else:
            client.connect(self.url,1883,60)


    def loop(self):
        client.loop_forever()





