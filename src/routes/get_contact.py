# Internal Function

from src.lib.managedb import ManageDb

# Fastapi

from fastapi import HTTPException, status


# Get single contact

def get_contact(id_contact):
    
    # Instantiating the class
    
    md = ManageDb()
    
    # Loading Database
    
    contacts = md.read_contacts()
 
    # Filtering by id
       
    for contact in contacts:
        if contact["id"] == id_contact:            
            return contact
    
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Contact not Found")