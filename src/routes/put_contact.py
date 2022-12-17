# Fastapi

from fastapi import HTTPException, status

# Internal Function

from src.lib.managedb import ManageDb



def put_contacts(id_contact, new_contact):
    
    # Instantiating the class
        
    md = ManageDb()
    
    # Loading Database
    
    contacts = md.read_contacts()
    
    # Validation if contact id exists
    
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            
            # Converting new contact in dictionary
            
            contacts[index] = new_contact.dict()
            
            # Validating if the contact has changes
            
            if new_contact.name == "":
                contacts[index]["name"] = contact["name"]
                
            if new_contact.phone == "":
                contacts[index]["phone"] = contact["phone"]
                
            # Written Contact
            
            md.write_contacts(contacts)
            return {
                "success": True,
                "message": "Updated contact"
            }
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Contact not Found")  
