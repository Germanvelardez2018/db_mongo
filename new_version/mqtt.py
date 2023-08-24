#! /usr/bin/env python3
import paho.mqtt.client as mqtt
from  new_version.db import DatabaseManager

    
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



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = msg.payload.decode('utf-8')
    data = data[:-1] # Elimino el ultimo elemento 
    print(f"{msg.topic} => {data}" )
    if(msg.topic =='RETCMD'):
        client.publish("OPT2","00:00:00:00", qos=2, retain=False) # Reinicio de comando
        return
    elif(msg.topic == "CMD"):
      elements = data.split("|")
    
      print(f"los valores obtenidos son {elements}")
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
            
    return




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(URL,1883,60)


class Connection():
    topics_sub = ["RETCMD","STATE","CMD","OPT2  "]
    
    
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
        




    def loop(self):
        client.loop_forever()




