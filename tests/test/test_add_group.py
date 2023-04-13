# -*- coding: utf-8 -*-

import pytest
from python_training.tests.model.group import Group
from python_training.tests.fixture.application import Application


# тест в файрфоксе

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="dcdc", header="cdcdc", footer="dcdccd"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
