import pytest
import string_to_int

TestCase1 = "42"
TestCase2 = "-42"
TestCase3 = "-4193 with words"
TestCase4 = "words and 987"
TestCase5 = "-91283472332"
TestCase6 = "   i    -45           am saurabh kumar.... 4 57jksadhkhsak@@@ 8 SADS 7 8    "

# @pytest.mark.skipif( reason="")
def test_string_to_integer_1():
    obj = string_to_int.Solution()
    assert obj.myAtoi(TestCase1) == 42


# @pytest.mark.skipif( reason="")
def test_string_to_integer_2():
    obj = string_to_int.Solution()
    assert obj.myAtoi(TestCase2) == -42

# @pytest.mark.skipif( reason="")
def test_string_to_integer_3():
    obj = string_to_int.Solution()
    assert obj.myAtoi(TestCase3) == -4193

# @pytest.mark.skip(reason="")
def test_string_to_integer_4():
    obj = string_to_int.Solution()
    assert obj.myAtoi(TestCase4) == 0

# @pytest.mark.skip(reason="")
def test_string_to_integer_5():
    obj = string_to_int.Solution()
    assert obj.myAtoi(TestCase5) == 0

# @pytest.mark.skip(reason="")
def test_string_to_integer_6():
    obj = string_to_int.Solution()
    assert obj.myAtoi(TestCase6) == 0


