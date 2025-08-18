# Демо-проект по автоматизации UI и API уровней приложения Contact List App

> <a target="_blank" href="https://thinking-tester-contact-list.herokuapp.com/">Ссылка на сайт</a>
----
### Проект реализован с использованием:
<img src="resources/python-original.svg" width="50"><img src="resources/pytest-original.svg" width="50"><img src="resources/selenium-original.svg" width="50"><img src="resources/selene.png" width="50"><img src="resources/jenkins-original.svg" width="50"><img src="resources/selenoid.png" width="50"><img src="resources/allure_report.png" width="50"><img src="resources/allure-test-ops.png" width="50"><img src="resources/tg.png" width="50">

----

### Особенности проекта

* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Запуск UI тестов в Selenoid
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Оповещения о тестовых прогонах в Telegram

 ### Список проверок, реализованных в UI и API автотестах

#### Регистрация

- [x] Успешная регистрация пользователя.
- [x] Регистрация пользователя, не заполнены обязательные поля.
- [x] Регистрация пользователя, email уже зарегистрирован.

#### Авторизация

- [x] Успешная авторизация пользователя.
- [x] Авторизация пользователя, некорректные email/password.

#### Добавление контакта

- [x] Успешное добавление контакта, заполнены все данные.
- [x] Добавление контакта, не заполнены обязательные поля.

#### Изменение контакта

- [x] Успешное изменение всех данных контакта.
- [x] Изменение данных контакта, не заполнены обязательные поля.

#### Удаление контакта

- [x] Успешное удаление контакта.

____

### Локальный запуск
> Для локального запуска необходимо выполнить команды:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
----

### Удаленный запуск автотестов выполняется в Jenkins или в Allure TestOps
> <a href="https://jenkins.autotests.cloud/job/20_goncharenko_filipp_contact_list_demo/">Ссылка на проект в Jenkins</a>

> <a href="https://allure.autotests.cloud/project/4886/dashboards/">Ссылка на проект в Allure TestOps</a>

#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/20_goncharenko_filipp_contact_list_demo/">проект</a>
2. Нажать кнопку `Build Now`
3. Результат запуска сборки можно посмотреть в отчёте Allure, в запуске Allure TestOps

#### Для запуска автотестов в Allure TestOps

1. Открыть <a target="_blank" href="https://allure.autotests.cloud/project/4886/dashboards">проект</a>
2. В боковом меню перейти на вкладку "Джобы".
3. Кликнуть кнопку "Запустить джобу" у `20_goncharenko_filipp_contact_list_demo`
4. В открывшемся модальном окне при необходимости указать название и другую мета-информацию.
5. Кликнуть на кнопку "Отправить".
6. Отслеживать выполнение можно на вкладке<a target="_blank" href="https://allure.autotests.cloud/project/4886/launches">"Запуски"</a>.


----

### Параметры pytest при локальном запуске

<code>pytest .</code> – запуск всех тестов.

<code>pytest -m api</code> – запуск API тестов.

<code>pytest -m ui</code> – запуск UI тестов.


### Allure отчет


#### Общие результаты
<img src="resources/allure_overview.png" alt="Allure отчет. Общие результаты." width="800">

#### Список тест кейсов в Allure 
<img src="resources/allure_test_cases.png" alt="Allure отчет. Список тест кейсов в Allure." width="800">

#### Пример тест кейса в Allure с логированием и вложениями
<img src="resources/allure_test_sample.png" alt="Allure отчет. Пример тест кейса в Allure" width="400">

### Allure TestOps

#### Примеры запуска в Allure TestOps
<img src="resources/allure_test_ops_1.png" alt="Allure TestOps 1" width="800">
<br>
<img src="resources/allure_test_ops_2.png" alt="Allure TestOps 2" width="800">
<br>
<img src="resources/allure_test_ops_3.png" alt="Allure TestOps 3" width="800">

#### Нотификация в Telegram
<img src="resources/tg_report.png" alt="Telegram notification" width="400">

#### Видео прохождения теста Web
<img src="resources/test_gif.gif" alt="test video" width="800">