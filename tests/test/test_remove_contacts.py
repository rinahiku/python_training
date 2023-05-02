def test_cancel_removing(app):
    app.contact.cancel_removing_contacts()


def test_remove_contact(app):
    app.contact.del_first_contact()


def test_remove_all_contacts(app):
    app.contact.del_all_contacts()
