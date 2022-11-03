from test.test_data.users import hellen
from model.pages.registration_form import *
from model.controls.date import *


def test_registration_form():
    # GIVEN
    given_opened()

    # ARRANGE
    set_first_name(hellen.name)
    set_last_name(hellen.last_name)
    set_email(hellen.email)
    set_gender(hellen.gender)
    set_number(hellen.user_number)
    #date_picker(hellen.birth_month, hellen.birth_year, hellen.birth_day)
    date_birth(hellen.date_of_birth)
    upload_picture('resources/qa-2-min.png')
    set_adress(hellen.current_address)
    set_state_dropdown(hellen.state)
    set_city(hellen.city)
    set_hobbies()
    add_subjects(hellen.subjects)
    submit_form()

    # ACT
    should_have_submitted(
        [
            ('Student Name', f'{hellen.name} {hellen.last_name}'),
            ('Student Email', hellen.email),
            ('Gender', hellen.gender.value),
            ('Mobile', hellen.user_number),
            ('Date of Birth', hellen.date_of_birth),
            ('Subjects', hellen.subjects),
            ('Hobbies', hellen.hobbies),
            ('Picture', hellen.picture_file),
            ('Address', hellen.current_address),
            ('State and City', f'{hellen.state} {hellen.city}')
        ],
    )
