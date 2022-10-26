import unittest
import Checkers


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.workers = Checkers.Workers

    def test_check_ru_true(self):
        self.assertEqual(self.workers.check_ru("а"), True)

    def test_check_ru_false(self):
        self.assertEqual(self.workers.check_ru("F"), False)

    def test_check_letter(self):
        self.assertEqual(self.workers.check("прора"), True)

    def test_check_replace(self):
        self.assertEqual(self.workers.hangman_replace("а", "абабаб", "______"), ["_б_б_б", "а_а_а_"])


if __name__ == '__main__':
    unittest.main()
