import pytest
from tachycardia import case_space_remove


@pytest.mark.parametrize("string_1, string_out1", [
                ("aBc ", "abc"),
                ("ABC", "abc"),
                (" AbC", "abc"),
                ("AbC? ", "abc?")
])
def test_case_space_remove(string_1, string_out1):
    assert case_space_remove(string_1) == string_out1
