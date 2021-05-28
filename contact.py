class Contact:
    """
    Class that generates new instance of contacts

    """

    contact_list =[]
    def  __init__(self, first_name, last_name, number):
            self.first_name= first_name
            self.last_name= last_name
            self.number= number
    
          
    def save(self):
        self.contact_list.append(self)
    
    @staticmethod
    def displays_all_contacts():
        """
        displays all the contacts stored in the
        contact_list
        """
        return Contact.contact_list 

    @classmethod
    def delete_contact(cls, contact):
         """deletes the contact from the list"""
         Contact.contact_list.remove(contact) 
                  
    