import pytest
from tachycardia import case_space_remove, remove_punc


@pytest.mark.parametrize("string_1, string_out1", [
                ("aBc ", "abc"),
                ("ABC", "abc"),
                (" AbC", "abc"),
                ("AbC? ", "abc?")
])
def test_case_space_remove(string_1, string_out1):
    assert case_space_remove(string_1) == string_out1


@pytest.mark.parametrize("string_2, string_out2", [
                ("Hello?", "Hello"),
                ("Hello!?", "Hello"),
                ("?Hello*", "Hello"),
                ("Hello/ ", "Hello ")
])
def test_remove_punc(string_2, string_out2):
    assert remove_punc(string_2) == string_out2
