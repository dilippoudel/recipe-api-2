"""Sample tests."""
from django.test import SimpleTestCase
from app.test_module import calc, greetings

class CalcTests(SimpleTestCase):
    """Test the calc modult.""" 
    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
        
class GreetingTest(SimpleTestCase):
    """Test the greeting according to the age."""
    def test_greeting_check(self):
        res = greetings.define_greeting(15, 'Rabin')
        self.assertEqual(res, 'Oi Rabin ! k garya xas ?')