import pytest

from homework.person_descriptior import person_descriptior


def test_should_return_mlody_when_20_given():
    # When
    result = person_descriptior(20)
    # Then
    assert result == str("Młody")

def test_should_return_mlody_when_7_given():
    # When
    result = person_descriptior(7)
    # Then
    assert result == str("Nastolatek")

def test_should_return_dojrzaly_when_40_given():
    # When
    result = person_descriptior(40)
    # Then
    assert result == str("Dojrzały")

def test_should_return_wiekowy_when_60_given():
    # When
    result = person_descriptior(60)
    # Then
    assert result == str("Wiekowy")

def test_should_return_na_emeryturze_when_77_given():
    # When
    result = person_descriptior(77)
    # Then
    assert result == str("Na emeryturze")


def test_should_raise_value_error_when_less_0():
    with pytest.raises(ValueError):
        person_descriptior(-1)


