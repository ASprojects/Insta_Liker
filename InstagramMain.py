from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/?hl=pl')
        time.sleep(5)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(7)
        try:
            bot.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        except Exception as ex:
            time.sleep(10)


    def like_pic(self,hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'/?hl=pl')
        time.sleep(5)
        for i in range(1,5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
        posts = bot.find_elements_by_class_name('v1Nh3')
        links = [elem.find_element_by_css_selector('a').get_attribute('href') for elem in posts]
        for link in links:
            bot.get(link)
            time.sleep(5)
            try:
                bot.find_element_by_class_name('_8-yf5 ').click()
                time.sleep(5)
            except Exception as ex:
                time.sleep(60)

###adam = InstaBot('email', 'haslo')
###adam.login()
###adam.like_pic('hashtag')
