import sqlite3
from models.contact import Contact

class ContactDAO:
    def __init__(self, db_path='contacts.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                surname1 TEXT,
                                surname2 TEXT,
                                job_title TEXT,
                                company TEXT,
                                street TEXT,
                                ext_number TEXT,
                                int_number TEXT,
                                neighborhood TEXT,
                                city TEXT,
                                state TEXT,
                                postal_code TEXT,
                                phone TEXT,
                                email TEXT,
                                birth_date TEXT,
                                age INTEGER
                              )''')
        self.conn.commit()

    def add_contact(self, contact: Contact):
        self.cursor.execute('''INSERT INTO contacts (name, surname1, surname2, job_title, company, street, ext_number, 
                                                      int_number, neighborhood, city, state, postal_code, phone, email, 
                                                      birth_date, age)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                              (contact.name, contact.surname1, contact.surname2, contact.job_title, contact.company, 
                               contact.street, contact.ext_number, contact.int_number, contact.neighborhood, 
                               contact.city, contact.state, contact.postal_code, contact.phone, contact.email, 
                               contact.birth_date, contact.age))
        self.conn.commit()

    def get_all_contacts(self):
        self.cursor.execute("SELECT * FROM contacts")
        rows = self.cursor.fetchall()
        contacts = []
        for row in rows:
            contacts.append(Contact(*row))
        return contacts

    def update_contact(self, contact_id, updated_contact_data):
        contact = updated_contact_data

        if updated_contact_data.birth_date:
            contact.age = contact.calculate_age()

        self.cursor.execute('''UPDATE contacts
                                SET name = ?, surname1 = ?, surname2 = ?, job_title = ?, company = ?, street = ?, 
                                ext_number = ?, int_number = ?, neighborhood = ?, city = ?, state = ?, postal_code = ?,
                                phone = ?, email = ?, birth_date = ?, age = ?
                            WHERE id = ?''', 
                            (contact.name, contact.surname1, contact.surname2, contact.job_title, 
                                contact.company, contact.street, contact.ext_number, contact.int_number,
                                contact.neighborhood, contact.city, contact.state, contact.postal_code,
                                contact.phone, contact.email, contact.birth_date, contact.age, contact_id))

        self.conn.commit()

    def delete_contact(self, contact_id):
        self.cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        self.conn.commit()

    def get_contact_by_id(self, contact_id):
        self.cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
        row = self.cursor.fetchone()
        if row:
            return Contact(*row)
        return None

    def close(self):
        self.conn.close()
