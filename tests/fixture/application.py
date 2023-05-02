from selenium import webdriver
from tests.fixture.session import SessionHelper
from tests.fixture.group import GroupHelper
from tests.fixture.contacts import ContactHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not len(wd.find_elements_by_link_text("home page")) > 0 or len(wd.find_elements_by_name("user")) > 0 or len(wd.find_elements_by_link_text("add new")) > 0:
            wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def clear_cookie(self):
        self.wd.delete_all_cookies()

    def destroy(self):
        self.wd.quit()
