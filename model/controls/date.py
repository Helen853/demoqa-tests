from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys


def date_picker(month, year, day):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(
        f'.react-datepicker__day--0{day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()


def date_birth(date: str):
    browser.element('#dateOfBirthInput').send_keys(Keys.COMMAND + 'a').type(date).press_enter()