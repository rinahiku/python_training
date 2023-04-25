
def test_cancel_removing(app):
    app.session.login(username="admin", password="secret")
    app.contact.cancel_removing_contacts()
    app.session.logout()
    app.clear_cookie()


def test_remove_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_first_contact()
    app.session.logout()
    app.clear_cookie()


def test_remove_all_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_all_contacts()
    app.session.logout()
    app.clear_cookie()

