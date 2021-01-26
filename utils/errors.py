class ElementIsNotTypeInt(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class ArgumentIsNotTypeList(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class MissingSellPrice(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)