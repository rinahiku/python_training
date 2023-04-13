import pytest
from python_training.tests.model.contact import Contact
from python_training.tests.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


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
