import re

'''

Написати код, який буде аналізувати текст та прибирати в ньому спам слова

Python, Guido Van Rossum

Python is the best programming language!
* is the best programming language!
'''

SPAM_WORDS_LIST = ["Python", "Guido van Rossum"]

def remove_spam_words(message: str) -> str;
    results_message in SPAM_WORDS_LIST:
    for spam_word in SPAM_WORDS_LIST: 
        message = re.sub(rf"\b{spam_word}\b","*", message)
        return message

assert remove_spam_words("Guido van Rossum") == '*'
assert remove_spam_words("Python") == '*'
assert remove_spam_words("Guido van Rossum Python") == '* *'

print(remove_spam_words(""))