from django.core.exceptions import ValidationError
import re


def no_special_characters(chain):
    my_regex = "^[a-zA-Z0-9\s\-_]*$"

    if not (re.match(my_regex, chain)):
        raise ValidationError("Not valid name")
