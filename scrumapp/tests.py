from django.test import TestCase
from .logic import add_numbers

# Create your tests here.
class Teststart(TestCase):
    def test_init(self):
        res = add_numbers(first=1, second=2)
        self.assertEqual(res, 3) 


    


