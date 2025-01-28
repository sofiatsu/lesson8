import string

def is_palindrome(text):
    lower_text = text.lower()
    no_spaces_text = lower_text.replace(' ', '')
    for p in string.punctuation:
        no_spaces_text = no_spaces_text.replace(p, "")
    reversed_text = no_spaces_text[::-1]
    if no_spaces_text == reversed_text:
        return True
    return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")