import unittest
from Sydney_millon_test1 import is_palindrome, get_time_based_greeting, get_time_based_farewell, process_input

class TestConsoleApp(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("python"))

    def test_process_input(self):
        self.assertEqual(process_input("radar"), ("Bien dit!", "Well said!", "Хорошо сказано!"))
        self.assertEqual(process_input("hello"), "hello")

    def test_time_based_greetings(self):
        greeting = get_time_based_greeting()
        self.assertIn(greeting, [("Bonjour", "Good morning", "Доброе утро"), 
                                ("Bonne après-midi", "Good afternoon", "Добрый день"),
                                ("Bonsoir", "Good evening", "Добрый вечер"),
                                ("Bonne insomnie", "Good night", "Доброй ночи"),
                                ("Bon réveil", "Good awakening", "Доброе утро")])

    def test_time_based_farewells(self):
        farewell = get_time_based_farewell()
        self.assertIn(farewell, [
        "Au revoir, bonne matinée, Goodbye, good morning, До свидания, доброе утро",
        "Au revoir, bonne après-midi, Goodbye, good afternoon, До свидания, добрый день",
        "Au revoir, bonne soirée, Goodbye, good evening, До свидания, добрый вечер",
        "Au revoir, bonne nuit, Goodbye, good night, До свидания, спокойной ночи"
    ])

if __name__ == '__main__':
    unittest.main()
