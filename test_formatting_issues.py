# Intentional formatting issues for testing
def test_function():pass

class TestClass:
    def method(self):return True
    def another_method(  self  ):
        x=1+2
        return x
        
# Bad import ordering
from django.contrib import admin
import os
from django.db import models
import sys
