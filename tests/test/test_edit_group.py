from tests.model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="hkhkh", header="v,,v", footer="as;d;f"))
    app.session.logout()
    app.clear_cookie()
