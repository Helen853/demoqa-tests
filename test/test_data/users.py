from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Physics'
    Chemistry = 'Chemistry'
    Economics = 'Economics'
    Biology = 'Biology'
    English = 'English'


class Hobbies(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    name: str
    gender: Gender
    last_name: str = 'Dudareva'
    email: str = 'dudarevalen_197@mail.ru'
    user_number: str = '8919860276'
    date_of_birth: str = '28 December,1997'
    birth_day: str = '28'
    birth_month: str = 'december'
    birth_year: str = '1997'
    subjects: Tuple[str] = 'Maths'
    hobbies: Tuple[str] = 'Sports'
    current_address: str = 'vostok'
    state: str = 'NCR'
    city = 'Gurgaon'


hellen = User(name='Hellen', gender=Gender.Female)
