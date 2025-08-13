from faker import Faker
from dataclasses import dataclass, field


fake = Faker()

@dataclass
class RandomUser:
    first_name: str = fake.first_name()
    last_name: str = fake.last_name()
    email: str = f'{first_name}.{last_name}@{fake.domain_name()}'.lower()
    password: str = field(
        default=fake.password(
            length=12,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True
        ),
        repr=False)
