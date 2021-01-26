class Operator:
    pass

class Equals(Operator):
    def __str__(self) -> str:
        return "="

class GreaterThan(Operator):
    def __str__(self) -> str:
        return ">"

class LessThan(Operator):
    def __str__(self) -> str:
        return "<"

class IN(Operator):
    def __str__(self) -> str:
        return "IN"

class NOT_IN(Operator):
    def __str__(self) -> str:
        return "NOT IN"

