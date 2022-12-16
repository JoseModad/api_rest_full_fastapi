# Fastapi

from fastapi import FastAPI, HTTPException, status

# Funciones Internas

from src.lib.managedb import ManageDb

# Instancias
## Fastapi

app = FastAPI()


## Base de Datos(Json)

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
      