
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.urls import reverse
import platform

class AccountTests(StaticLiveServerTestCase):

    fixtures = ['fixtures/users.json', 'fixtures/news.json', 'fixtures/cat.json']
    
    def setUp(self):
        os_used = platform.system()
        if os_used == "Linux":
            self.browser = webdriver.Chrome('account/chromedriver_linux')
        elif os_used == "Windows":
            self.browser = webdriver.Chrome('account/chromedriver.exe')       
        elif os_used == "Darwin":
            self.browser = webdriver.Chrome('account/chromedriver_mac')

        self.browser = webdriver.Chrome('account/chromedriver_linux')
        self.browser.get(self.live_server_url)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.close()
    
    
    def test_login(self):
        username='user'
        password='user'

        self.browser.find_element_by_link_text('Login').click()

        username_input = self.browser.find_element_by_id('inputUsername')
        password_input = self.browser.find_element_by_id('inputPassword')

        username_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(3)
        self.browser.find_element_by_class_name('btn-block').click()
        
        looged_user_username = self.browser.find_element_by_class_name('dropdown-toggle').text
        
        self.assertEquals(looged_user_username, username.capitalize())
   
    def test_register(self):

        self.browser.find_element_by_link_text('Register').click()
        
        username_input  = self.browser.find_element_by_id('inputUsername')
        email_input     = self.browser.find_element_by_id('inputEmail')
        password1_input = self.browser.find_element_by_id('inputPassword1')
        password2_input = self.browser.find_element_by_id('inputPassword2')
        date_input      = self.browser.find_element_by_id('inputDob')

        username ='Test'
        password = 'aksjd8f7u*ASD*Aydajksnd'

        username_input.send_keys(username)
        email_input.send_keys('test@gmail.com')
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        date_input.send_keys('01/02/2000')
        self.browser.find_element_by_class_name('btn-block').click()

        time.sleep(3)
        registered_user_username = self.browser.find_element_by_class_name('dropdown-toggle').text

        self.assertEquals(registered_user_username, username.capitalize())
        

        
   
