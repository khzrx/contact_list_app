from faker import Faker


fake = Faker()

class RandomUser:
    def __init__(self):
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = f'{self.first_name}.{self.last_name}@{fake.domain_name()}'.lower()
        self.password = fake.password(
            length=12,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True
        )

    def __repr__(self):
        return f'first_name = {self.first_name}, last_name = {self.last_name}, '\
               f'email = {self.email}, password = {len(self.password) * "*"}'
