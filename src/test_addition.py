import sys
import os

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from addition import add

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
