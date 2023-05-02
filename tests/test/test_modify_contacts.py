from tests.model.contact import Contact


def test_modify_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact()
        app.contact.create_new(Contact(firstname="Alex", lastname="Ivanov", phone_mobile='9999999'))
    app.contact.modify_first_contact(Contact(firstname="dsv"))
