# Intentional formatting issues for testing
def test_function():pass

class TestClass:
    def method(self):return True
    def another_method(  self  ):
        x=1+2
        return x
        
import os
import sys

# Bad import ordering
from django.contrib import admin
from django.db import models
