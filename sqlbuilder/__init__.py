from sqlbuilder.errors import UnknownSQLType
from sqlbuilder.queries import SelectStatement, DeleteStatement


class SQLStatementFactory:
    """[summary]
    """

    @staticmethod
    def build(selector: str):
        """[summary]

        :param selector: [description]
        :type selector: str
        :raises UnknownSQLType: [description]
        :return: [description]
        :rtype: [type]
        """
        if selector in ("select", "SELECT"):
            return SelectStatement()
        elif selector in ("delete", "DELETE"):
            return DeleteStatement()
        else:
            raise UnknownSQLType("Supported types are SELECT, UPDATE and DELETE not {}".format(selector))









