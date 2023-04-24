from tests.model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="dsv", middlename="dddd", lastname="aaaa",
                                   nickname="sdc dvdv",
                                   title="fcv vv ", company=" sdfsdf",
                                   address="sdfsdf", phone_home="11111",
                                   phone_mobile="22222",
                                   phone_work="33333",
                                   fax="13121", email="sdfdsf", email2="sdf", email3="sdf",
                                   homepage="fsdv", bday="1",
                                   bmonth="May", address2="dsv", phone2="sdv", notes="sv"))
    app.session.logout()
    app.clear_cookie()
