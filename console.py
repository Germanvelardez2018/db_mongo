
from  new_version.db import DatabaseManager
from pprint import pprint
from new_version.mqtt import Connection





class Console:

    def __init__(self,config = {}):
        topics_sub = ["SHADOW","RETCMD","STATE","CMD","EXC"]

        self.db = DatabaseManager(config)
        self.connection = Connection(topics_sub)



        


if __name__ == "__main__":
    print("iniciando programa")
    WALL = Console()
    WALL.connection.loop()
    
      