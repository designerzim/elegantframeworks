import pytest
from titlecase import title_case


class TitleCaseTests:
    @pytest.mark.parametrize(('initial_text', 'expected_text'), [
        ('this should be capitalized', 'This Should Be Capitalized'),
        ('ALL CAPS', 'All Caps'),
        ('a furry friend', 'a Furry Friend'),
        ('hop on pop', 'Hop on Pop'),
        ('by from to at on nor for or but and the an a', 'by from to at on nor for or but and the an a'),
    ])
    def test_text_is_uppercase(self, initial_text, expected_text):
        returned_text = title_case(initial_text)
        assert returned_text == expected_text
