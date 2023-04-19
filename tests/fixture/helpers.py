from tests.fixture.session import SessionHelper
from tests.fixture.group import GroupHelper
from tests.fixture.contacts import ContactHelper


class AllHelpers:
    def __init__(self):
        self.group = GroupHelper
        self.contacts = ContactHelper
        self.session = SessionHelper
