import uuid
from datetime import datetime
import time
from enum import Enum
from decimal import Decimal

from tortoise.fields import DatetimeField

LITERALS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def get_new_referral_code():
    value = int(time.time() * 100000)
    res = ""
    for i in range(9):
        m = int(value % 36)
        value = value / 36

        res = LITERALS[m] + res

    return res[:3] + "-" + res[3:6] + "-" + res[6:]


class CustomDatetimeField(DatetimeField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_python_value(self, *args, **kwargs):
        value = super().to_python_value(*args, **kwargs)
        if isinstance(value, datetime):
            return value.replace(tzinfo=None)
        return value

    def to_db_value(self, *args, **kwargs):
        value = super().to_db_value(*args, **kwargs)
        if isinstance(value, datetime):
            return value.replace(tzinfo=None)
        return value


class TimestampMixin:
    created_at = CustomDatetimeField(null=True, auto_now_add=True)
    updated_at = CustomDatetimeField(null=True, auto_now=True)


class ToDictMixin:

    def to_dict(self, serialize_keys=None):
        serialize_keys = serialize_keys or self.serialize_keys
        result = dict()
        for key in serialize_keys:
            value = getattr(self, key)
            if isinstance(value, uuid.UUID):
                value = str(value)
            if isinstance(value, datetime):
                value = value.strftime("%d %b %y, %H:%M:%S")
            if isinstance(value, Enum):
                value = value.value
            if isinstance(value, Decimal):
                value=str(value)
            result[key] = value


        return result


