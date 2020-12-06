
import time
import platform

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.urls import reverse


class AccountTests(StaticLiveServerTestCase):

    fixtures = ['fixtures/users.json', 'fixtures/news.json', 'fixtures/cat.json', 'fixtures/comment.json']
    
    def setUp(self):
        os_used = platform.system()
        if os_used == "Linux":
            self.browser = webdriver.Chrome(executable_path='/opt/app-root/src/account/chromedriver_linux')
        elif os_used == "Windows":
            self.browser = webdriver.Chrome(executable_path='/opt/app-root/src/account/chromedriver.exe')       
        elif os_used == "Darwin":
            self.browser = webdriver.Chrome(executable_path='/opt/app-root/src/account/chromedriver_mac')
            
        self.browser.get(self.live_server_url)
        self.browser.maximize_window()

        # Log in
        username='user'
        password='user'
        self.browser.find_element_by_link_text('Login').click()
        username_input = self.browser.find_element_by_id('inputUsername')
        password_input = self.browser.find_element_by_id('inputPassword')
        username_input.send_keys(username)
        password_input.send_keys(password)
        self.browser.find_element_by_class_name('btn-block').click()

    def tearDown(self):
        self.browser.close()
    
    def test_like_acticle(self):

        # Open an article 
        self.browser.find_element_by_id('article-button').click()
        time.sleep(3)
        # Get the current likes
        current_likes = self.browser.find_element_by_id('1').text
        time.sleep(3)
        # Like the article
        self.browser.find_element_by_id('like-button').click()
        time.sleep(3)
        # Get updated likes
        updated_likes = self.browser.find_element_by_id('1').text

        # when like button is clicked it should change the like count
        # this is confirmed by comparing initial like count by like count 
        # after the button is clicked 
        self.assertNotEqual(current_likes, updated_likes)


    def test_comment_acticle(self):

        test_comment = "This is a testing comment"

        # Open an article 
        self.browser.find_element_by_id('article-button').click()
        time.sleep(3)

        # Add comment 
        self.browser.find_element_by_id('new_comment_button').click()
        time.sleep(1)

        # Get text area element 
        text_area = self.browser.find_element_by_id('textarea')

        # Add text to the text area
        text_area.clear()
        text_area.send_keys(test_comment)

        # click submit button
        self.browser.find_element_by_class_name('post-but').click()
        time.sleep(3)
        # grab the comment from the DOM 
        comment_content = self.browser.find_element_by_id('comment-content-3').text 

        # Compare inserted comment with the rendered one
        self.assertEqual(test_comment, comment_content)

        # get the comment count before deletion
        comment_count_before_deletion = self.browser.find_element_by_class_name('comments-count').text

        # delete the comment 
        self.browser.find_element_by_id('delete_comment').click()
        time.sleep(3)

        # get the comment count after deletion
        comment_count_after_deletion = self.browser.find_element_by_class_name('comments-count').text

        # compare comment count before and after deletion - not equal
        self.assertNotEqual(comment_count_before_deletion, comment_count_after_deletion)







