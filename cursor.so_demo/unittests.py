def is_palindrome(s):
    return s == s[::-1]

import unittest

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome('radar'))
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome(''))
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('world'))

if __name__ == '__main__':
    unittest.main()