import os

from selene.support.conditions import be, have
from selene.support.shared import browser


def test_sending_practice_form(open_browser):
    browser.element('#firstName').should(be.blank).type('Oksana')
    browser.element('#lastName').should(be.blank).type('Prokopenko')
    browser.element('#userEmail').should(be.blank).type('proyeillepebe-2165@yopmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1998"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="0"]').click()
    browser.element('.react-datepicker__day--005').click()
    browser.element('#subjectsInput').should(be.blank).type('arts').press_enter()
    browser.element('[for=hobbies-checkbox-1').click()
    browser.element('[for=hobbies-checkbox-3').click()
    browser.element('#uploadPicture').set_value(
            os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'file/test_5.jpeg')))
    browser.element('#currentAddress').should(be.blank).type('Краснодарский край')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text(
    'Oksana' and
    'Prokopenko' and
    'proyeillepebe-2165@yopmail.com' and
    'Male' and
    '1234567890' and
    '01 January, 1998' and
    'Arts' and
    'Sports' and 'Music' and
    'test_5.jpeg' and
    'Краснодарский край' and
    'NCR Noida'
    ))










