from faker import Faker
from dataclasses import dataclass, field


fake = Faker()

@dataclass
class RandomUser:
    first_name: str = field(default_factory=fake.first_name)
    last_name: str = field(default_factory=fake.last_name)
    email: str = field(init=False)
    password: str = field(
        default_factory=lambda: fake.password(
            length=12,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True
        ),
        repr=False)

    def __post_init__(self):
        self.email = f'{self.first_name}.{self.last_name}@{fake.domain_name()}'.lower()

    def as_dict(self):
        return {
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'password': self.password
        }