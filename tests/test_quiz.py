import pytest  
from selenium import webdriver  
import time
from simbirproject.pages.quiz_page import QuizPage

URL = 'https://practice-automation.com/form-fields/'

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver  
    driver.quit()


def test_input_all_data(browser):
    quiz_page = QuizPage(browser)
    quiz_page.open(URL)
    
    quiz_page.enter_name('mansur')
    quiz_page.enter_password('password123')
    quiz_page.set_favourite_drinks()
    quiz_page.set_favourite_color()
    quiz_page.set_automation_list_value()
    quiz_page.enter_email('name@example.com')
    quiz_page.enter_message()

    assert quiz_page.submit() == QuizPage.MESSAGE_RECEIVED
    
def test_enter_all_butno_name(browser):
    quiz_page = QuizPage(browser)
    quiz_page.open(URL)
    
    quiz_page.enter_password('password123')
    quiz_page.set_favourite_drinks()
    quiz_page.set_favourite_color()
    quiz_page.set_automation_list_value()
    quiz_page.enter_email('name@example.com')
    quiz_page.enter_message()
    
    assert quiz_page.submit() == QuizPage.FORM_ERROR