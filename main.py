# Fastapi

from fastapi import FastAPI, HTTPException, status

# Funciones Internas

from src.lib.managedb import ManageDb

# Pydantic

from pydantic import BaseModel

# Python

from uuid import uuid4 as uuid


# Class

class ContactModel(BaseModel):
    id: str = str(uuid())
    name: str
    phone: str



# Instances

## Fastapi

app = FastAPI()


## Data Base(Json)

md = ManageDb()


# Routes

## Home

@app.get("/")
def root():
    return {"message": "This is Fastapi"}


## Get all contacts

@app.get("/api/contacts")
def get_all_contacts():
    return md.read_contacts()
    

## Get single contact
    
@app.get("/api/contacts/{id_contact}", status_code = status.HTTP_200_OK)
def get_single_contact(id_contact: str):
    
    # Loading Database
    
    contacts = md.read_contacts()
 
    # Filtering by id
       
    for contact in contacts:
        if contact["id"] == id_contact:            
            return contact
    
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Contact not Found")  


## Creating new Contact

@app.post("/api/contacts")
def add_contact(new_contact: ContactModel):
    contacts = md.read_contacts() 
    
    # Converting new contact in dictionary
       
    new_contact = new_contact.dict()
    
    # Adding new contact to dictionary
    
    contacts.append(new_contact)
    
    # Writing changes
    
    md.write_contacts(contacts)
    return {
        "success": True,
        "message": "Added new Contact"
    }
  
 
 # Update Contact
 
@app.put("/api/contacts/{id_contact}")
def update_contact(id_contact: str, new_contact: ContactModel):   
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


# Delete Contact
 
@app.delete("/api/contacts/{id_contact}")
def remove_contact(id_contact: str):   
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