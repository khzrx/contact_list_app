import allure
from allure_commons.types import Severity
from contact_list_app.pages.login_page import login_page
from contact_list_app.pages.registration_page import registration_page
from contact_list_app.pages.contact_list_page import contact_list_page


@allure.parent_suite('UI')
@allure.suite('Регистрация и авторизация')
@allure.sub_suite('Регистрация')
@allure.epic('Регистрация и авторизация')
@allure.feature('Регистрация пользователя')
@allure.story('Пользователь должен иметь возможность зарегистрироваться на сайте')
class TestRegistration:

    @allure.title('Успешная регистрация пользователя.')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('UI', 'Регистрация')
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

