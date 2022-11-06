from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import resources


def to_resource(relative_path):
    return str(Path(resources.__file__).parent.joinpath(relative_path).absolute())


service = Service(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=service)