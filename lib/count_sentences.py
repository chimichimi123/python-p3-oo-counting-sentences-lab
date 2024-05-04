#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            self._value = ''
            print("The value must be a string.")
        else:
            self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')
    
    def count_sentences(self):
      count = 0
      words = self._value.split(' ')
      for word in words:
        if word and word[-1] in '.?!':
          count += 1
      return count if self._value else 0