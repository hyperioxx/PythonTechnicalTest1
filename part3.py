""" 
I didn't have enough time to implement everything i wanted too 
"""


import unittest
import datetime
from sqlbuilder import SQLStatementFactory
from sqlbuilder.errors import UnknownSQLType, OperatorNotValid
from sqlbuilder.operations import Equals, GreaterThan, LessThan, IN, NOT_IN
from sqlbuilder.table import Id, Url, Date, Rating

TABLE_NAME = "tableName"

class TestSQLBuilder(unittest.TestCase):

    def test_sql_factory(self):
        self.assertRaises(UnknownSQLType, SQLStatementFactory.build, 1)

    def test_basic_select(self):
        expected = "SELECT id, url, date, rating FROM tableName WHERE id = 1 ;" 
        Query = SQLStatementFactory.build("SELECT")
        Query.from_(TABLE_NAME)
        Query.where(Id(), Equals(), 1)
        self.assertEqual(str(Query), expected)

    def test_basic_delete(self):
        expected = "DELETE  FROM tableName WHERE id = 1 ;"
        Query = SQLStatementFactory.build("DELETE")
        Query.from_(TABLE_NAME)
        Query.where(Id(), Equals(), 1)
        self.assertEqual(str(Query), expected)
        
    def test_wrong_operator(self):
        Query = SQLStatementFactory.build("SELECT")
        Query.from_(TABLE_NAME)
        self.assertRaises(OperatorNotValid, lambda: Query.where(Date(), IN() , "1 Jan 2016"))



if __name__ == '__main__':
    unittest.main()