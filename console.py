
from  new_version.db import DatabaseManager
from pprint import pprint
from new_version.mqtt import Connection





class Console:

    def __init__(self,config = {}):
      
       self.db = DatabaseManager(config)
       print("before conection")
       self.connection = Connection()



        


if __name__ == "__main__":
    print("iniciando programa")
    WALL = Console()
    WALL.connection.loop()
    
      