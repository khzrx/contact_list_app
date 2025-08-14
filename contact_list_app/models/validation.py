from dataclasses import dataclass


@dataclass
class RegistrationValidationTexts:
    required_fields : str = 'User validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required., email: Email is invalid, password: Path `password` is required.'
    email_in_use: str = 'Email address is already in use'

@dataclass
class AuthorizationValidationTexts:
    incorrect_login_or_password = 'Incorrect username or password'

@dataclass
class AddContactValidationTexts:
    required_fields = 'Contact validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required.'

@dataclass
class EditContactValidationTexts:
    required_fields = 'Validation failed: lastName: Path `lastName` is required., firstName: Path `firstName` is required.'