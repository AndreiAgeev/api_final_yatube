from typing import Any
from rest_framework.serializers import ValidationError


class SameUser:
    message = "You can't follow yourself"

    def __call__(self, value) -> Any:
        if value['user'] == value['following']:
            raise ValidationError(self.message)
