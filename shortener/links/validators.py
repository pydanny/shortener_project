from django.core.exceptions import ValidationError


def validate_five_characters(value):
    print value
    if len(value) < 5:
        msg = u"Custom identifiers must have at least 5 characters"
        raise ValidationError(msg)
