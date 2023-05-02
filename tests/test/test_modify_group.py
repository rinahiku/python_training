from tests.model.group import Group


def test_modify_group_name(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test", header="olala", footer="ananan"))
    app.group.modify_first_group(Group(name="New group"))
