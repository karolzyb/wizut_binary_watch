import pytest
from safety_check import *
import sys
from mock import patch

def test_000():
    assert safety_check('12') == None

# def test_001():
#     assert safety_check('12') == True


def test_function():
  with patch('sys.exit') as exit_mock:
    safety_check([0,1])
    assert exit_mock.called