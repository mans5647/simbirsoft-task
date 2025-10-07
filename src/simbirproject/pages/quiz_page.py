from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.common.exceptions import NoAlertPresentException

class QuizPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        
    MESSAGE_RECEIVED = 1
    FORM_ERROR = -1
    
    locators = {
        'username': (By.ID, 'name-input'),
        'password': (By.XPATH, '/html/body/div[1]/div[2]/div/div/main/div/article/div/form/label[2]/input'),
        'email': (By.ID, 'email'),
        'message': (By.ID, 'message'),
        'drink1': (By.ID, 'drink1'),
        'drink2': (By.ID, 'drink2'),
        'drink3': (By.ID, 'drink3'),
        'drink4': (By.ID, 'drink4'),
        'drink5': (By.ID, 'drink5'),
        'favourite_color': (By.ID, 'color3'),
        'automation': (By.ID, 'automation')
    }
    
    def open(self, url):
        self.driver.get(url)
        
    def enter_name(self, name):  
        self.username.set_text(name)
        
    def enter_password(self, passwd):
        self.password.set_text(passwd)
    
    def enter_email(self, email):
        self.email.set_text(email)
    
    def enter_message(self):
        ul_list = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/main/div/article/div/form/ul')
        items = ul_list.find_elements(By.TAG_NAME, 'li')
        items_texts = [item.text for item in items]
        
        size = len(items_texts)
        longest_word = max(items_texts, key=len)
        self.message.set_text(f'{size}\r\n{longest_word}')
    
    def set_favourite_drinks(self):
        ActionChains(self.driver)\
            .scroll_to_element(self.drink2) \
            .perform()
        self.drink2.click_button()
        
        ActionChains(self.driver)\
            .scroll_to_element(self.drink3) \
            .perform()
        
        self.drink3.click_button()
    
    def set_favourite_color(self):
        ActionChains(self.driver)\
            .scroll_to_element(self.favourite_color) \
            .perform()
        self.favourite_color.click_button()
        
    def set_automation_list_value(self):
        ActionChains(self.driver)\
            .scroll_to_element(self.automation) \
            .perform()
        self.automation.select_element_by_value('yes')
    
    def submit(self) -> int:
        submit_btn = self.driver.find_element(By.XPATH, '//*[@id="submit-btn"]')
        ActionChains(self.driver)\
                .scroll_to_element(submit_btn) \
                .perform()
        submit_btn.click()
        wait = WebDriverWait(self.driver, 2)
        try:
            alert = wait.until(lambda d: d.switch_to.alert)
            return QuizPage.MESSAGE_RECEIVED    
        except NoAlertPresentException:
            pass
        
        return QuizPage.FORM_ERROR
