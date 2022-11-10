import allure
from selene.support.shared import browser
from model.controls import dropdown, modal
from selene import have, command
from selene.support.shared.jquery_style import ss

from typing import Tuple
from test.test_data.users import Subject, Gender

from utils.path import take_path


@allure.step('Открываем страницу регистрации')
def given_opened():
    browser.open('/automation-practice-form')
    ads = ss('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


@allure.step('Вводим имя')
def set_first_name(name: str):
    browser.element('#firstName').type(name)


@allure.step('Вводим фамилию')
def set_last_name(last_name: str) -> object:
    browser.element('#lastName').type(last_name)


@allure.step('Вводим адрес электронной почты')
def set_email(email: str):
    browser.element('#userEmail').type(email)


@allure.step('Выбираем пол')
def set_gender(gender: Gender):
    browser.all('[for^=gender-radio]').by(
        have.exact_text(gender.value)
    ).first.click()


@allure.step('Вводим телефонный номер')
def set_number(number: str):
    browser.element('#userNumber').type(number)


@allure.step('Загружаем фото')
def upload_picture(picture_file: str):
    browser.element('#uploadPicture').send_keys(take_path(picture_file))


@allure.step('Вводим адрес')
def set_adress(adress: str):
    browser.element('#currentAddress').type(adress)


@allure.step('Вводим город')
def set_city(city: str):
    browser.element('#react-select-4-input').type(city).press_enter()


@allure.step('Выбираем хобби')
def set_hobbies():
    browser.element('[for="hobbies-checkbox-1"][class="custom-control-label"]').click()


@allure.step('Выбираем предмет')
def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(values).press_enter()


@allure.step('Выбираем штат')
def set_state_dropdown(state):
    browser.element('#state').perform(command.js.scroll_into_view)
    dropdown.select(browser.element('#state'), state)


@allure.step('Жмем на кнопку подтверждения формы')
def submit_form():
    browser.element('#submit').press_enter()


@allure.step('Сверяем данные пользователя с данными формы')
def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
