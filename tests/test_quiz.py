import pytest  
from selenium import webdriver  

from tests.pages.quiz_page import QuizPage

URL = 'https://practice-automation.com/form-fields/'

@pytest.fixture
def browser():
    driver = webdriver.Chrome()

    yield driver  
    driver.quit()


def test_quiz_page(browser):
    quiz_page = QuizPage(browser)
    quiz_page.open(URL)
    
    quiz_page.enter_name('mansur')
    quiz_page.enter_password('password123')
    
    quiz_page.check_favourite_drinks()
    
    quiz_page.check_favourite_color()
    quiz_page.select_like_automation()
    quiz_page.enter_mock_email()
    quiz_page.enter_count_max_val()
    quiz_page.submit()
    
    assert quiz_page.has_name() and quiz_page.has_password()
    assert quiz_page.are_drinks_checked()
    assert quiz_page.is_favourite_color_checked()
    assert quiz_page.check_if_selected_automation()
    assert quiz_page.has_email()
    assert quiz_page.has_message()