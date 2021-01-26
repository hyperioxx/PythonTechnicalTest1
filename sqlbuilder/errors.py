class UnknownSQLType(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class OperatorNotValid(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)