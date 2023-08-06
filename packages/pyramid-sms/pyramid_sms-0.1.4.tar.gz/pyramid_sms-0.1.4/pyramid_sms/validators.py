"""Some Colander phone number validators."""
import colander

from .utils import normalize_us_phone_number
from .utils import normalize_international_phone_number


def valid_us_phone_number(node, value):
    """Checks if a phone number looks like a valid US mobile number after normalization.

    :raise: colander.Invalid on error
    """

    assert type(value) == str, "Phone number must be string type"

    normalized = normalize_us_phone_number(value)

    if not normalized.startswith("+1"):
        raise colander.Invalid(node, "Not a US phone number")

    if len(normalized) != 12:
        raise colander.Invalid(node, "Phone number doesn't have correct count of digits")


def valid_international_phone_number(node, value):
    """Checks if a phone number looks like a international number after normalization.

    :raise: colander.Invalid on error
    """

    assert type(value) == str, "Phone number must be string type"

    normalized = normalize_international_phone_number(value)

    if not normalized.startswith("+"):
        raise colander.Invalid(node, "Start international phone number with + (plus sign)")

    if len(normalized) < 7:
        raise colander.Invalid(node, "Phone number must be at least 7 digits")




