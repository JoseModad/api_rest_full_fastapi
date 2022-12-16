# Python

import pathlib
import json


class ManageDb:
    
    # Getting the route we are on and taking it to /src/db/dbcontacts.json
    
    __address_file = "{0}/src/db/dbcontacts.json".format(pathlib.Path().parent.absolute())
    
    # Reading contacts
    
    def read_contacts(self):
       with open(self.__address_file, "r") as data:
           
            # Converting db to json       
           
           return json.loads(data.read())


    # Write a new contact

    def write_contacts(self, new_data):
        with open(self.__address_file, "w") as data:
            data.write(json.dumps(new_data))
