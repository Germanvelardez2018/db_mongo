#! /usr/bin/env python3
import paho.mqtt.client as mqtt
from  new_version.db import DatabaseManager
from colorama import Fore, Back, Style, init

init() # Colorama

db = DatabaseManager({})


MSG_CMD =[
    "CONFIGURO INTERVALO ",
    "CONFIGURO MAXIMO DE MUESTRAS",
    "FORZAR EXTRACCION DE INFORMACION ",
    "MODO DEBUG",
    "FLAGS"
]



USER_ID = "INTI"
URL = "broker.hivemq.com"
RETURN_COMAND = "00:00:00:00"
last_command = None




# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Conectado a servicio MQTT")



def _get_date(data):
    """
    Extrae la fecha de la nmea gps
    """
    elements = data.split(',')
    if elements == "":
        return None
    return  elements[0],elements[0][1:9]


def _insert_data(id,date,data):
            json = {}
            json["num"]=id
            json["data"]=data
            obj = db.find_data(date,**{"num":id})           
            if obj == None:
                print(Fore.BLUE + f"dato insertado:{json}")
                print(Style.RESET_ALL)
                db.insert_data(date,**json)





# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global last_command
    data = msg.payload.decode('utf-8')
    topic = str(msg.topic)

    if topic == 'SHADOW':
        params = data.split(':')
        index =  int((params[0]))
        if index >0:
            print(f"[APLICACION]=>{MSG_CMD[index-1]}")
            print(Style.RESET_ALL)
        last_command = data
    elif(topic == "RETCMD"):
        print(f"{data}<=[drifter]")      
        client.publish("SHADOW",RETURN_COMAND,qos=1,retain=False)
    elif(msg.topic == "CMD"):
      data = data[:-1]
      elements = data.split("|")
      for _data in elements:
        id,date = _get_date(_data)
        if date :
            _insert_data(id,date,_data)
      
        else:
            print(Fore.RED+"dato invalido, descartar")
            print(Style.RESET_ALL)
    elif(topic == 'STATE'):
        print(Fore.GREEN+f"{data}<= [drifter]")
        print(Style.RESET_ALL)
        if last_command:
            counter = 0  
            while counter <100:     
                client.publish("OPT",last_command,qos=1,retain=True)
                counter+=1
            last_command = None
    else:
        #print(f"{topic}=>{data}")
        pass
        
    










client = mqtt.Client()
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




