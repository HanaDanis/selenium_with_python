import sys
sys.path.insert(0, r'C:\Users\Hana Danis\Downloads\Bootcamp-automation\python\HtmlPro')
from Testes.test_home import *

from selenium.webdriver.common.by import By

class LocatorsHome:
    firstname_locator = (By.NAME, "fname")
    lastname_locator = (By.NAME, "lname")
    city_locator = (By.NAME, "City")
    email_locator = (By.ID, "email")
    area_locator = (By.NAME, "areaCode")
    phone_locator = (By.ID, "phone")
    male_locator = (By.ID, "m")
    female_locator = (By.ID, "f")
    other_locator = (By.ID, "o")
    math_locator = (By.NAME, "math")
    physics_locator = (By.NAME, "pyhs")
    pop_locator = (By.XPATH, "//input[@id='m' and @name='gender']")
    dud_locator = (By.ID, "//input[@id='o' and @name='gender']")
    biology_locator = (By.ID, "b")
    chem_locator = (By.ID, "c")
    english_locator = (By.ID, "e")
    clear_locator = (By.ID, "CB")
    send_locator = (By.ID, "send")
    jsPara_locator = (By.ID, "pbyuser")
    setText_locator = (By.XPATH, "//button[text()='Set Text']")
    links_locator = (By.TAG_NAME, "a")
    nextpage_locator = (By.NAME, "nextPage")
    windy_locator = (By.NAME, "myLink")
    tera_locator = (By.NAME, "myLinkTS")
    java_locator = (By.NAME, "notMyLink")
