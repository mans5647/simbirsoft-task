from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class QuizPage:
    def __init__(self, driver: Chrome):
        self._driver = driver
    
    def open(self, url):
        self._driver.get(url)
        
    def enter_name(self, name):  
        self._driver.find_element(By.ID, "name-input").send_keys(name)
    
    def enter_password(self, passwd):
        self._driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/label[2]/input").send_keys(passwd)
    
    def has_name(self) -> bool:
        return self._driver.find_element(By.ID, "name-input").get_attribute('value') != ''
    
    def has_password(self) -> bool:
        return self._driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/label[2]/input").get_attribute('value') != ''
    
    # whats is your favourite drink
    def check_favourite_drinks(self):
        names = ['drink2', 'drink3']
        wait = WebDriverWait(self._driver, 100)
        for name in names:
            elem = self._driver.find_element(By.ID, name)
            ActionChains(self._driver)\
                .scroll_to_element(elem) \
                .perform()
            elem.click()
        
    def are_drinks_checked(self) -> bool:
        names = ['drink2', 'drink3']
        selected_ = []
        for i in names:
            selected_.append(self._driver.find_element(By.ID, i).is_selected())

        return all(selected_)
    
    def check_favourite_color(self):
        wait = WebDriverWait(self._driver, 100)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="color3"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="color3"]')))
        elem = self._driver.find_element(By.XPATH, '//*[@id="color3"]')
        
        ActionChains(self._driver)\
                .scroll_to_element(elem) \
                .perform()
        elem.click()
    
    def is_favourite_color_checked(self) -> bool:
        return self._driver.find_element(By.ID, 'color3').is_selected()
    
    def select_like_automation(self):
        select_element = self._driver.find_element(By.NAME, 'automation')
        ActionChains(self._driver)\
                .scroll_to_element(select_element) \
                .perform()
        select = Select(select_element)
        select.select_by_value('yes')
    
    def check_if_selected_automation(self):
        select_element = self._driver.find_element(By.NAME, 'automation')
        select = Select(select_element)
        return select.first_selected_option.get_attribute('value') == 'yes'
    
    
    def enter_mock_email(self):
        self._driver.find_element(By.ID, 'email').send_keys('name@example.com')
    
    def has_email(self):
        return self._driver.find_element(By.ID, 'email').get_attribute('value') != ''
    
    def enter_count_max_val(self):
        ul_list = self._driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/main/div/article/div/form/ul')
        items = ul_list.find_elements(By.TAG_NAME, 'li')
        items_texts = [item.text for item in items]
        
        message_input = self._driver.find_element(By.ID, 'message')
        size = len(items_texts)
        longest_word = max(items_texts, key=len)
        message_input.send_keys(f'{size}\r\n')
        message_input.send_keys(f'{longest_word}')
    
    def has_message(self):
        return self._driver.find_element(By.ID, 'message').get_attribute('value') != ''
        
    def submit(self):
        submit_btn = self._driver.find_element(By.XPATH, '//*[@id="submit-btn"]')
        ActionChains(self._driver)\
                .scroll_to_element(submit_btn) \
                .perform()
        submit_btn.click()
        wait = WebDriverWait(self._driver, 2)
        alert = wait.until(lambda d: d.switch_to.alert)
        text = alert.text
        print(text)