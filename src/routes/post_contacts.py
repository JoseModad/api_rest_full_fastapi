from src.lib.managedb import ManageDb



def post_contacts(new_contact):
    
    # Instantiating the class
    
    md = ManageDb()
    
    # Loading database
    
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