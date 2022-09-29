import os.path

from selene import have, be
from selene.support.shared import browser

from test.test_data.users import hellen


def test_registration_form():
    browser.open('/automation-practice-form')

    # ARRANGE
    browser.element('#firstName').type(hellen.name)
    browser.element('#lastName').type(hellen.last_name)
    browser.element('#userEmail').type(hellen.email)
    browser.all('[for^=gender-radio]').by(
        have.exact_text(hellen.gender.value)
    ).first.click()
    browser.element('#userNumber').type(hellen.user_number)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type(hellen.birth_month)
    browser.element('.react-datepicker__year-select').type(hellen.birth_year)
    browser.element(f'.react-datepicker__day--0{hellen.birth_day}').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_data/qa-2-min.png'))
    browser.element('#currentAddress').type(hellen.current_address)
    browser.element('#react-select-3-input').type(hellen.state).press_enter()
    browser.element('#react-select-4-input').type(hellen.city).press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()

    for subject in hellen.subjects:
        browser.element('#subjectsInput').type(hellen.subjects).press_enter()

    browser.element('#submit').press_enter()

    # ACT
    browser.element('#example-modal-sizes-title-lg').should(be.visible).should(
        have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text(hellen.name))
    browser.element('.table-responsive').should(have.text(hellen.email))
    browser.element('.table-responsive').should(have.text(hellen.gender.value))
    browser.element('.table-responsive').should(have.text(hellen.user_number))
    browser.element('.table-responsive').should(have.text(hellen.date_of_birth))
    browser.element('.table-responsive').should(have.text(hellen.subjects))
    browser.element('.table-responsive').should(have.text(hellen.hobbies))
    browser.element('.table-responsive').should(have.text(hellen.current_address))
    browser.element('.table-responsive').should(have.text(f'{hellen.state} {hellen.city}'))
