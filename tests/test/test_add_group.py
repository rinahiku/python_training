from tests.model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="dcdc", header="cdcdc", footer="dcdccd"))
    app.session.logout()
    app.clear_cookie()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
    app.clear_cookie()
