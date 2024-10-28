from faker import Faker
import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.contact import Contact

class RandomContactGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_contact(self):
        contact = Contact(
            name=self.faker.first_name(),
            surname1=self.faker.last_name(),
            surname2=self.faker.last_name(),
            job_title=self.faker.job(),
            company=self.faker.company(),
            street=self.faker.street_name(),
            ext_number=str(random.randint(100, 999)),
            int_number=str(random.randint(1, 30)),
            neighborhood=self.faker.city_suffix(),
            city=self.faker.city(),
            state=self.faker.state(),
            postal_code=self.faker.postcode(),
            phone=self.faker.phone_number(),
            email=self.faker.email(),
            birth_date=self.faker.date_of_birth(minimum_age=18, maximum_age=65).strftime("%Y-%m-%d")
        )
        return contact

if __name__ == "__main__":
    generator = RandomContactGenerator()

    random_contact = generator.generate_contact()
    print(vars(random_contact))
