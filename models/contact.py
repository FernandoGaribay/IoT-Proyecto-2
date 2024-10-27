from datetime import datetime

class Contact:
    def __init__(self, id=None, name="", surname1="", surname2="", job_title="", company="", street="", ext_number="",
                 int_number="", neighborhood="", city="", state="", postal_code="", phone="", email="", birth_date="", age=None):
        self.id = id
        self.name = name
        self.surname1 = surname1
        self.surname2 = surname2
        self.job_title = job_title
        self.company = company
        self.street = street
        self.ext_number = ext_number
        self.int_number = int_number
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone = phone
        self.email = email
        self.birth_date = birth_date

        if age is not None:
            self.age = age
        else:
            self.age = self.calculate_age()

    def calculate_age(self):
        birth_date = datetime.strptime(self.birth_date, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))