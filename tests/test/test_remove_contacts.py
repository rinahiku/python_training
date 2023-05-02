from tests.model.contact import Contact


def test_cancel_removing(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact()
        app.contact.create_new(Contact(firstname="Alex", lastname="Ivanov", phone_mobile='9999999'))
    app.contact.cancel_removing_contacts()


def test_remove_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact()
        app.contact.create_new(Contact(firstname="Alex", lastname="Ivanov", phone_mobile='9999999'))
    app.contact.del_first_contact()


def test_remove_all_contacts(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact()
        app.contact.create_new(Contact(firstname="Alex", lastname="Ivanov", phone_mobile='9999999'))
    app.contact.del_all_contacts()
