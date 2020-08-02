import pytest
from fibonacci.fibonacci import fibonacci
def test_should_return_13_when_given_7():
    # When
    result = fibonacci(7)
    # Then
    assert result == 13