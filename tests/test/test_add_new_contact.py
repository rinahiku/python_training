from tests.model.contact import Contact


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.create_new(Contact(firstname="Elena", middlename="Nikolaevna", lastname="Troshina",
                                   nickname="rina",
                                   title="qa", company="effective technologies",
                                   address="nizhniy novgorod", phone_home="+79991201201",
                                   phone_mobile="+7900000000",
                                   phone_work="+7911111111111",
                                   fax="1111", email="lina@LINA.ru", email2="asd", email3="asddd",
                                   homepage="ddddd", bday="11",
                                   bmonth="September", address2="dkskdkdk", phone2="mmmm", notes="dkkkk"))
    app.session.logout()
    app.clear_cookie()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.create_new(Contact(firstname="", middlename="", lastname="",
                                   nickname="",
                                   title="", company="",
                                   address="", phone_home="",
                                   phone_mobile="",
                                   phone_work="",
                                   fax="", email="", email2="", email3="",
                                   homepage="", bday="-",
                                   bmonth="-", address2="", phone2="", notes=""))
    app.session.logout()
    app.clear_cookie()
