from faker import Faker
from dataclasses import dataclass, field


fake = Faker()

@dataclass
class RandomContact:
    first_name: str = field(default_factory=fake.first_name)
    last_name: str = field(default_factory=fake.last_name)
    birthdate: str = field(default_factory=lambda: fake.date_of_birth().strftime('%Y-%m-%d'))
    email: str = field(init=False)
    phone: str = field(default_factory=lambda: str(fake.random_number(digits=10, fix_len=True)))
    street_address_1: str = field(default_factory=fake.street_address)
    street_address_2: str = field(default_factory=fake.street_address)
    city: str = field(default_factory=fake.city)
    state: str = field(default_factory=fake.state)
    postal_code: str = field(default_factory=fake.postalcode)
    country: str = field(default_factory=fake.country)

    def __post_init__(self):
        self.email = f'{self.first_name}.{self.last_name}@{fake.domain_name()}'.lower()

    def as_dict(self):
        return {
            'firstName': self.first_name,
            'lastName': self.last_name,
            'birthdate': self.birthdate,
            'email': self.email,
            'phone': self.phone,
            'street1': self.street_address_1,
            'street2': self.street_address_2,
            'city': self.city,
            'stateProvince': self.state,
            'postalCode': self.postal_code,
            'country': self.country
        }