from tests.model.group import Group


def test_add_group(app):
    app.group.create(Group(name="dcdc", header="cdcdc", footer="dcdccd"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
