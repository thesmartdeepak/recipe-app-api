'''Test Addition service'''
from django.test import SimpleTestCase
from app.services import add_two_numbers

class AdditionTest(SimpleTestCase):

    '''Test for service'''
    def test_addition_service(self):
        res = add_two_numbers(5, 6)
        self.assertEqual(res, 11)