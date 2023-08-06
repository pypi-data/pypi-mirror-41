from pyramid_sms.utils import normalize_us_phone_number
from pyramid_sms.utils import normalize_international_phone_number


def test_normalize_us_phone_number():
    assert normalize_us_phone_number("555 123 1234") == "+15551231234"
    assert normalize_us_phone_number("+1 555 123 1234") == "+15551231234"
    assert normalize_us_phone_number("+1 555 (123) 1234") == "+15551231234"
    assert normalize_us_phone_number("5551231234") == "+15551231234"
    assert normalize_us_phone_number("005551231234") == "+15551231234"



def test_normalize_international_phone_number():
    assert normalize_international_phone_number("00 555 123 1234") == "+15551231234"
    assert normalize_international_phone_number("+1 555 123 1234") == "+15551231234"
