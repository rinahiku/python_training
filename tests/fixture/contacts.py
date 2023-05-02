from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_name("firstname", contact.firstname)
        self.change_field_name("middlename", contact.middlename)
        self.change_field_name("lastname", contact.lastname)
        self.change_field_name("nickname", contact.nickname)
        self.change_field_name("title", contact.title)
        self.change_field_name("company", contact.company)
        self.change_field_name("address", contact.address)
        self.change_field_name("home", contact.phone_home)
        self.change_field_name("mobile", contact.phone_mobile)
        self.change_field_name("work", contact.phone_work)
        self.change_field_name("fax", contact.fax)
        self.change_field_name("email", contact.email)
        self.change_field_name("email2", contact.email2)
        self.change_field_name("email3", contact.email3)
        self.change_field_name("homepage", contact.homepage)
        self.change_date_of_birth("bday", contact.bday)
        self.change_date_of_birth("bmonth", contact.bmonth)
        self.change_field_name("address2", contact.address2)
        self.change_field_name("phone2", contact.phone2)
        self.change_field_name("notes", contact.notes)

    def create_new(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()

    def del_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # SELECT FIRST CONTACT
        wd.find_element_by_name("selected[]").click()
        # DELETE FIRST CONTACT
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # SUBMIT DELETION
        wd.switch_to.alert.accept()

    def del_all_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        # SELECT ALL CONTACTS
        wd.find_element_by_id("MassCB").click()
        # DELETE ALL CONTACTS
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # SUBMIT DELETION
        wd.switch_to.alert.accept()

    def cancel_removing_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        # SELECT ALL CONTACTS
        wd.find_element_by_id("MassCB").click()
        # DELETE ALL CONTACTS
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # DISMISS
        wd.switch_to.alert.dismiss()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def change_field_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_date_of_birth(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def count_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))