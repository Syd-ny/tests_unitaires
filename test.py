import unittest
from Sydney_millon_test1 import is_palindrome, get_time_based_greeting, get_time_based_farewell, process_input

class TestConsoleApp(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("python"))

    def test_process_input(self):
        self.assertEqual(process_input("radar"), ("Bien dit!", "Well said!", "Хорошо сказано!"))
        self.assertEqual(process_input("hello"), "hello")

    # These tests might need to be adjusted depending on the time of day they are run
    def test_time_based_greetings(self):
        greeting = get_time_based_greeting()
        self.assertIn(greeting, [("Bonjour", "Good morning", "Доброе утро"), 
                                ("Bonne après-midi", "Good afternoon", "Добрый день"),
                                ("Bonsoir", "Good evening", "Добрый вечер"),
                                ("Bonne insomnie", "Good night", "Доброй ночи"),
                                ("Bon réveil", "Good awakening", "Доброе утро")])

    def test_time_based_farewells(self):
        farewell = get_time_based_farewell()
        self.assertIn(farewell, ["Au revoir, bonne matinée",
                                 "Au revoir, bonne après-midi",
                                 "Au revoir, bonne soirée",
                                 "Au revoir, bonne nuit"])

if __name__ == '__main__':
    unittest.main()
