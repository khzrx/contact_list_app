import allure
import pytest
from allure_commons.types import Severity
from contact_list_app.pages.login_page import login_page
from contact_list_app.pages.contact_list_page import contact_list_page
from contact_list_app.models import validation


validation_texts = validation.AuthorizationValidationTexts()

@allure.parent_suite('UI')
@allure.suite('Регистрация и авторизация')
@allure.sub_suite('Авторизация')
@allure.epic('Регистрация и авторизация')
@allure.feature('Авторизация пользователя')
@allure.story('Пользователь должен иметь возможность авторизоваться на сайте')
@pytest.mark.ui
class TestAuthorization:

    @allure.title('Успешная авторизация пользователя.')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Авторизация')
    @allure.label('owner', 'fdgoncharenko')
    def test_authorization_user_successful(self):
        login_page.open()

        login_page.type_email()
        login_page.type_password()
        login_page.click_submit_button()

        contact_list_page.logout_button_should_be_clickable()

    @allure.title('Авторизация пользователя, некорректные email/password.')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Авторизация', 'Валидация')
    @allure.label('owner', 'fdgoncharenko')
    def test_authorization_user_incorrect_email_or_password(self):
        login_page.open()

        login_page.type_email()
        login_page.password_input.type('1234')
        login_page.click_submit_button()

        login_page.check_validation_error_text(validation_texts.incorrect_login_or_password)
