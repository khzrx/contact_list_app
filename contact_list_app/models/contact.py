from faker import Faker
from dataclasses import dataclass


fake = Faker()

@dataclass
class RandomContact:
    first_name: str = fake.first_name()
    last_name: str = fake.last_name()
    birthdate: str = fake.date_of_birth().strftime('%Y-%m-%d')
    email: str = f'{first_name}.{last_name}@{fake.domain_name()}'.lower()
    phone: str = str(fake.random_number(digits=10, fix_len=True))
    street_address_1: str = fake.street_address()
    street_address_2: str = fake.street_address()
    city: str = fake.city()
    state: str = fake.state()
    postal_code: str = fake.postalcode()
    country: str = fake.country()
