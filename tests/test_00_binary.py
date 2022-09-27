import pytest
from binary_gpio_operations import *

@pytest.mark.parametrize(
"x,y,result",
   [
       (12, 4, [1,1,0,0]),
       (4, 4, [0,1,0,0]),
       (5, 3, [1,0,1]),
       (8, 5, [0,1,0,0,0])
   ]
)

def test_001(x, y, result):
    assert int_to_bin_list(x, y) == result

def test_002():
    assert int_to_bin_list(12, 3) == [1,1,0,0]

# def test_001():
#     assert int_to_bin_list(12, 3) == [0,0,0,0,0]