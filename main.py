# Fastapi

from fastapi import FastAPI, status

# Internal functions

from src.routes.get_contact import get_contact
from src.routes.get_contacts import get_contacts
from src.routes.post_contacts import post_contacts
from src.routes.put_contact import put_contacts
from src.routes.delete_contact import delete_contacts

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


# Routes

## Home

@app.get("/")
def root():
    return {"message": "This is Fastapi"}


## Get all contacts

@app.get("/api/contacts")
def get_all_contacts():
    return get_contacts()
    

## Get single contact
    
@app.get("/api/contacts/{id_contact}", status_code = status.HTTP_200_OK)
def get_single_contact(id_contact: str):
    return get_contact(id_contact)
    

## Creating new Contact

@app.post("/api/contacts")
def add_contact(new_contact: ContactModel):
    return post_contacts(new_contact)
  
 
 # Update Contact
 
@app.put("/api/contacts/{id_contact}")
def update_contact(id_contact: str, new_contact: ContactModel):   
    return put_contacts(id_contact, new_contact)


# Delete Contact
 
@app.delete("/api/contacts/{id_contact}")
def remove_contact(id_contact: str):   
    return delete_contacts(id_contact)