from python_training.tests.fixture.session import SessionHelper
from python_training.tests.fixture.group import GroupHelper
from python_training.tests.fixture.contacts import ContactHelper


class AllHelpers:
    def __init__(self):
        self.group = GroupHelper
        self.contacts = ContactHelper
        self.session = SessionHelper
