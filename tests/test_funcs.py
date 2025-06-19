from mx.funcs import (
    sf,
    sf3,
    sf4,
    sf5,
)


def test_sf():
    """Test sf function."""
    assert sf(0) == 0
    assert sf(123456789,2) == 120000000
    assert sf(0.00123456789,3) == 0.00123
    assert sf(123456789.987654321,4) == 123500000.0
    assert sf(-123456789) == -123000000
    assert sf(-0.00123456789) == -0.00123

def test_sf3():
    """Test sf3 function."""
    assert sf3(0) == 0
    assert sf3(123456789) == 123000000
    assert sf3(0.00123456789) == 0.00123
    assert sf3(123456789.987654321) == 123000000.0
    assert sf3(-123456789) == -123000000
    assert sf3(-0.00123456789) == -0.00123

def test_sf4():
    """Test sf4 function."""
    assert sf4(0) == 0
    assert sf4(123456789) == 123500000
    assert sf4(0.00123456789) == 0.001235
    assert sf4(123456789.987654321) == 123500000.0
    assert sf4(-123456789) == -123500000
    assert sf4(-0.00123456789) == -0.001235

def test_sf5():
    """Test sf5 function."""
    assert sf5(0) == 0
    assert sf5(123456789) == 123460000
    assert sf5(0.00123456789) == 0.0012346
    assert sf5(123456789.987654321) == 123460000.0
    assert sf5(-123456789) == -123460000
    assert sf5(-0.00123456789) == -0.0012346
