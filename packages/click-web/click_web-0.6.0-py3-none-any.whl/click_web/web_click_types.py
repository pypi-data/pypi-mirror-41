"""
Module contains click types that could be useful on web pages and provide form validation by just setting type.
"""
import re

import click


class EmailParamType(click.ParamType):
    name = 'email'
    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    def convert(self, value, param, ctx):
        if self.EMAIL_REGEX.match(value):
            return value
        else:
            self.fail(f'{value} is not a valid email', param, ctx)


EMAIL_TYPE = EmailParamType()
