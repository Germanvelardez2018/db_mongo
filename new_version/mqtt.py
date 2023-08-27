#! /usr/bin/env python3
import paho.mqtt.client as mqtt
from  new_version.db import DatabaseManager
import time
    
db = DatabaseManager({})

USER_ID = "INTI"
URL = "broker.hivemq.com"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Conectado a servicio MQTT "+str(rc))



def get_date(data):
    print(f"extraer datos de {data}")
    elements = data.split(',')
    if elements == "":
        return None
    return  elements[0],elements[0][1:9]


last_command = None
shadow_flag = 1 

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global last_command
    global shadow_flag 
    data = msg.payload.decode('utf-8')
    topic = str(msg.topic)
    if topic == 'SHADOW':
        print(f"peticion de comando {data}")
        last_command = data
    elif(topic == "RETCMD"):
        print(f"{topic}=>{data}")      
        client.publish("SHADOW","00:00:00:00",qos=2,retain=True)
    elif(msg.topic == "CMD"):
      data = data[:-1]
      elements = data.split("|")
      for e in elements:
        id,date = get_date(e)
        if date :
            print(f"dato valido")
            json = {}
            json["num"]=id
            json["data"]=e
            obj = db.find_data(date,**{"num":id})           
            if obj == None:
                print(f"dato insertado:{json}")
                db.insert_data(date,**json)
        else:
            print("dato invalido, descartar")
    elif(topic == 'STATE'):
       
        print(f"{topic}=>{data}")
        if last_command:
            counter = 0  
            while counter <100:     
                client.publish("OPT",last_command,qos=2,retain=True)
                counter+=1
            last_command = None
    else:
        #print(f"{topic}=>{data}")
        pass
        
    

    




client = mqtt.Client(client_id="INTI2023")
client.on_connect = on_connect
client.on_message = on_message
client.connect(URL,1883,60)


class Connection():
    topics_sub = ["SHADOW","RETCMD","STATE","CMD","OPT"]
    
    
    def __init__(self,user_id = USER_ID,url = URL,sub_topic = None ) -> None:
        self.id = user_id
        self.url = url
        for topic in self.topics_sub:
            client.subscribe(topic)





    def loop(self):
        client.loop_forever()




