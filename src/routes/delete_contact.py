# Fastapi

from fastapi import HTTPException, status

# Internal Function

from src.lib.managedb import ManageDb



def delete_contacts(id_contact):

    # Instantiating the class
        
    md = ManageDb()
    
    # Loading Database

    contacts = md.read_contacts()
    
    # Validation if contact id exists
    
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            
            # Remove contact
            
            contacts.pop(index)
            
            md.write_contacts(contacts)
            
            return {
            "success": True,
            "message": "Deleted Contact"
        }
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)