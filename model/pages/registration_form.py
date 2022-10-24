from selene.support.shared import browser
from model.controls import dropdown, modal
from selene import have, command
from selene.support.shared.jquery_style import ss

from typing import Tuple
from test.test_data.users import Subject, Gender

import os


def given_opened():
    browser.open('/automation-practice-form')
    ads = ss('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def set_first_name(name: str):
    browser.element('#firstName').type(name)


def set_last_name(last_name: str):
    browser.element('#lastName').type(last_name)


def set_email(email: str):
    browser.element('#userEmail').type(email)


def set_gender(gender: Gender):
    browser.all('[for^=gender-radio]').by(
        have.exact_text(gender.value)
    ).first.click()


def set_number(number: str):
    browser.element('#userNumber').type(number)


def upload_picture(picture_file: str):
    browser.element('#uploadPicture').send_keys(os.path.abspath(picture_file))


def set_adress(adress: str):
    browser.element('#currentAddress').type(adress)


def set_city(city: str):
    browser.element('#react-select-4-input').type(city).press_enter()


def set_hobbies():
    browser.element('[for="hobbies-checkbox-1"][class="custom-control-label"]').click()


def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(values).press_enter()


def set_state_dropdown(state):
    browser.element('#state').perform(command.js.scroll_into_view)
    dropdown.select(browser.element('#state'), state)


def submit_form():
    browser.element('#submit').press_enter()


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
