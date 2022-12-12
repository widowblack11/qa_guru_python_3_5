import os

from selene.support.conditions import have
from selene.support.shared import browser


def test_sending_practice_form(open_browser):
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Oksana')  # ввод имени
    browser.element('#lastName').type('Prokopenko')  # ввод фамилии
    browser.element('#userEmail').type('proyeillepebe-2165@yopmail.com')  # вод эл почты
    browser.element('[for="gender-radio-2"]').click()  # выбор гендера
    browser.element('#userNumber').type('1234567890')  # ввод номера телефонов
    browser.element('#dateOfBirthInput').click()  # открытие формы выбора даты рождения
    browser.element('.react-datepicker__year-select').click()  # открытие выбора года рождения
    browser.element('.react-datepicker__year-select [value="1998"]').click()  # выбор года рождения
    browser.element('.react-datepicker__month-select').click()  # открытие формы выбора месяца рождения
    browser.element('.react-datepicker__month-select [value="0"]').click()  # выбор месяца рождения
    browser.element('.react-datepicker__day--005').click()  # выбор дня рождения
    browser.element('#subjectsInput').type('arts').press_enter()  # ввод предмета
    browser.element('[for=hobbies-checkbox-1').click()  # выбор хобби
    browser.element('[for=hobbies-checkbox-3').click()  # выбор хобби
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'file/test_5.jpeg')))  # загрузка файла
    browser.element('#currentAddress').type('Краснодарский край')  # ввод адрес
    browser.element('#react-select-3-input').type('NCR').press_enter()  # выбор штата
    browser.element('#react-select-4-input').type('Noida').press_enter()  # выбор города
    browser.element('#submit').press_enter()  # отправка формы

    # проверка соответствия отправленных данных в форме и полученных в итоговой таблицы после отправки заполненной
    # формы регистрации
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
