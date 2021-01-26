from sqlbuilder.operations import Equals, GreaterThan, LessThan, IN, NOT_IN

class Field:
    def __init__(self) -> None:
        self.allowed_operator = ()

    def check_allowed_op(self, op: object):
        return isinstance(op, self.allowed_operator)

class Id(Field):
    def __init__(self) -> None:
        super().__init__()
        self.allowed_operator = (Equals, GreaterThan, LessThan, IN, NOT_IN)

    def __str__(self) -> str:
        return "id"

class Url(Field):
    def __init__(self) -> None:
        super().__init__()
        self.allowed_operator = (Equals,)

    def __str__(self) -> str:
        return "url"

class Date(Field):
    def __init__(self) -> None:
        super().__init__()
        self.allowed_operator = (Equals, GreaterThan, LessThan)

    def __str__(self) -> str:
        return "date"


class Rating(Field):
    def __init__(self) -> None:
        super().__init__()
        self.allowed_operator = (Equals, GreaterThan, LessThan)

    def __str__(self) -> str:
        return "rating"






