from sqlbuilder.table import Field, Id, Url, Date, Rating
from sqlbuilder.errors import OperatorNotValid


class BaseStatement:

    def __init__(self) -> None:
        self.type = None
        self.table = None
        self.fields = [Id(), Url(), Date(), Rating()]
        self.where_clauses = []

    def _generate_statement(self) -> str:
        """Generates start of the SQL statment 

        :return: constructed sql statment 
        :rtype: str
        """
        return "{} {} FROM {} {} ;".format(self.type, ', '.join(str(p) for p in self.fields), self.from_, self._generate_where())

    def _generate_where(self) -> str:
        """ takes Where objects and builds a where statment

        :return: returns constructed where statment
        :rtype: str
        """
        where_statement = "WHERE "
        for idx, w in enumerate(self.where_clauses):
            where_statement += str(w)
            if idx != 0:
                where_statement += " AND "
        return where_statement

    def __str__(self) -> str:
        return self._generate_statement()
        

    def from_(self, table: str):
        """from table name 

        note - the alternative would be to use the @property decorator e.g.

            @property
            def from_:
                return self.from_

        :param from: name of database table
        :type from: str
        """
        self.from_ = table

    def where(self, field, op, value):
        """ Where clause builder 
        """
        self.where_clauses.append(Where(field, op, value))
        
    
class SelectStatement(BaseStatement):
    def __init__(self) -> None:
        super().__init__()
        self.type = "SELECT"

class UpdateStatement(BaseStatement):
    """ Currently not used 
    """
    def __init__(self) -> None:
        super().__init__()
        self.type = "UPDATE"

class DeleteStatement(BaseStatement):
    def __init__(self) -> None:
        super().__init__()
        self.type = "DELETE"
        self.fields = []

class Where:
    def __init__(self, field: object, op: object, value: object) -> None:
        if not field.check_allowed_op(op): raise OperatorNotValid(
            "{} is not a valid operation for current field {}".format(op, field)
            )

        self.field = field
        self.op = op

        if isinstance(value, list):
            self.value = "({})".format(", ".join(str(i) for i in value))
        else:
            self.value = value

    def __str__(self) -> str:
        return "{} {} {}".format(self.field, str(self.op), self.value)
