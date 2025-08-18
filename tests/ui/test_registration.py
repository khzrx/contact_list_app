import allure
import pytest
from allure_commons.types import Severity
from contact_list_app.pages.login_page import login_page
from contact_list_app.pages.registration_page import registration_page
from contact_list_app.pages.contact_list_page import contact_list_page
from contact_list_app.models import validation


validation_texts = validation.RegistrationValidationTexts()

@allure.parent_suite('UI')
@allure.suite('Регистрация и авторизация')
@allure.sub_suite('Регистрация')
@allure.epic('Регистрация и авторизация')
@allure.feature('Регистрация пользователя')
@allure.story('Пользователь должен иметь возможность зарегистрироваться на сайте')
@pytest.mark.ui
class TestRegistration:

    @allure.title('Успешная регистрация пользователя.')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Регистрация')
    @allure.label('owner', 'fdgoncharenko')
    def test_register_user_successful(self, random_user):
        login_page.open()
        login_page.click_signup_button()

        registration_page.type_first_name(random_user.first_name)
        registration_page.type_last_name(random_user.last_name)
        registration_page.type_email(random_user.email)
        registration_page.type_password(random_user.password)
        registration_page.click_submit_button()

        contact_list_page.logout_button_should_be_clickable()

    @allure.title('Регистрация пользователя, не заполнены обязательные поля.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('Регистрация', 'Валидация')
    @allure.label('owner', 'fdgoncharenko')
    def test_register_user_required_fields_not_filled(self):
        registration_page.open()

        registration_page.click_submit_button()

        registration_page.check_validation_error_text(validation_texts.required_fields)

    @allure.title('Регистрация пользователя, email уже зарегистрирован.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('Регистрация', 'Валидация')
    @allure.label('owner', 'fdgoncharenko')
    def test_register_user_email_in_use(self, random_user):
        registration_page.open()

        registration_page.type_first_name(random_user.first_name)
        registration_page.type_last_name(random_user.last_name)
        registration_page.type_email('test@test.com')
        registration_page.type_password(random_user.password)
        registration_page.click_submit_button()

        registration_page.check_validation_error_text(validation_texts.email_in_use)