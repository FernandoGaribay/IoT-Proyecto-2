from models.contact_dao import ContactDAO
from models.contact import Contact

class ContactController:
    def __init__(self, ui=None):
        self.contact_dao = ContactDAO()
        self.ui = ui

    def get_fields(self):
        id = self.ui.txt_idUsers.text()
        name = self.ui.txt_nameUsers.text()
        surname1 = self.ui.txt_lastNameFatherUsers.text()
        surname2 = self.ui.txt_lastNameMotherUsers.text()
        job_title = self.ui.txt_positionUsers.text()
        company = self.ui.txt_companyUsers.text()
        street = self.ui.txt_streetUsers.text()
        ext_number = self.ui.txt_extNumberUsers.text()
        int_number = self.ui.txt_intNumberUsers.text()
        neighborhood = self.ui.txt_neighborhoodUsers.text()
        city = self.ui.txt_municipalyUsers.text()
        state = self.ui.txt_stateUsers.text()
        postal_code = self.ui.txt_postalCodeUsers.text()
        phone = self.ui.txt_phoneUsers.text()
        email = self.ui.txt_emailUsers.text()
        birth_date = self.ui.txt_birthDayUsers.text()
        age = self.ui.txt_calculatedAgeUsers.text()
        
        return {
            "name": name,
            "surname1": surname1,
            "surname2": surname2,
            "job_title": job_title,
            "company": company,
            "street": street,
            "ext_number": ext_number,
            "int_number": int_number,
            "neighborhood": neighborhood,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "phone": phone,
            "email": email,
            "birth_date": birth_date
        }

    def add_contact(self, contact_data):
        contact = Contact(**contact_data)
        self.contact_dao.add_contact(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        contacts = self.contact_dao.get_all_contacts()
        return contacts

    def get_contact_by_id(self, id):
        contacts = self.contact_dao.get_contact_by_id(id)
        return contacts

    def update_contact(self, contact_id, column, new_value):
        self.contact_dao.update_contact(contact_id, column, new_value)
        print("Contact updated successfully!")

    def delete_contact(self, contact_id):
        self.contact_dao.delete_contact(contact_id)
        print("Contact deleted successfully!")

    def close_connection(self):
        self.contact_dao.close()