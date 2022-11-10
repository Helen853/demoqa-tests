from pathlib import Path

import allure

import resources


@allure.step('Строим полный путь до файла')
def take_path(relative_path: str):
    path = str(Path(__file__).parent.parent.joinpath('resources').joinpath(relative_path))
    return path
