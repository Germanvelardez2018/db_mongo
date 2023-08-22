
from db import database
from  new_version.db import DatabaseManager
from pprint import pprint
from new_version.mqtt import Connection

example_data ="{'_id': ObjectId('64e4c6b34fe40fc4cd46a781'), 'data': '\nsensor:temp:25.47,\n\tx:0.26-\n\ty:-0.01-\n\tz:1.11,\n\tgps:1:20230818185145.000:-34.576243:-58.517048:'}"




class Console:

    def __init__(self,config = {}):
      
       self.db = DatabaseManager(config)
       self.connection = Connection()



        


if __name__ == "__main__":
    WALL = Console()
    WALL.connection.loop()
    
      