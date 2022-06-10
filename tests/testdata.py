from faker import Faker


class TestData:
    """
    Test Data generator
    """
    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        self.password = fake.password()

