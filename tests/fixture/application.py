from selenium import webdriver
from python_training.tests.fixture.session import SessionHelper
from python_training.tests.fixture.group import GroupHelper
from python_training.tests.fixture.contacts import ContactHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()
