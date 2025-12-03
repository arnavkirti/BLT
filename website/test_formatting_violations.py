# Intentional formatting violations for testing

import sys,os,django
from django.db import models
import json

# Bad spacing around operators
def badly_formatted_function(  x,y,z  ):
    result=x+y+z
    return result

# Inconsistent quotes and spacing
def another_bad_function( a, b ):
    message = "This has 'mixed' quotes"
    data={'key':'value','another_key':'another_value'}
    return data

# Missing blank lines
class TestModel(models.Model):
    name = models.CharField(max_length=100)
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

# Trailing whitespace and bad indentation
def trailing_whitespace_function():
    x = 1   
    y = 2  
    if x > 0:
      return x + y
    else:
        return 0


# Another violation
def more_bad_formatting(  x  ,  y  ):
    return x+y
