"""
3.	Write a function that can define whether a word
is a Palindrome or not  (a word, phrase, or sequence
that reads the same backwards as forwards, e.g. madam)

"""
from unittest import TestCase

def is_palindrome(word):
    if type(word) == str and len(word) > 0:
        # reverse a word using [::-1]
        # then just check for equality as it should be the same
        return word == word[::-1]
    else:
        return 0

print(is_palindrome("madam")) # will print True
print(is_palindrome("apple")) # will print False
print(is_palindrome("")) # will print 0
print(is_palindrome(109)) # will print 0

"""
4.	Write tests for the newly created Palindrome function. 
Provide a brief explanation for your test case options. 
"""
class TestPalindrome(TestCase):
    """
    This test will check to see that it can
    correctly return true for a word that we
    know to be an actual palindrome
    """
    def test_correct_palindrome(self):
        actual = is_palindrome("madam")
        expected = True
        self.assertEqual(actual, expected)

    """
    This test will check to see that it can 
    correctly return False for a word that we 
    know to not be a palindrome
    """
    def test_incorrect_palindrome(self):
        actual = is_palindrome("apple")
        expected = False
        self.assertEqual(actual, expected)

    """
    This will check to see if the function
    will return a 0 if anything that is not
    a string inserted into it 
    """
    def test_incorrect_data_type(self):
        actual = is_palindrome(43770)
        expected = 0
        self.assertEqual(actual, expected)

    """
    This will check to see that the function 
    will return a 0 if the string is empty
    """
    def test_incorrect_string_length(self):
        actual = is_palindrome("")
        expected = 0
        self.assertEqual(actual, expected)


