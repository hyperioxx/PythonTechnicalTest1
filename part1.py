import unittest

def increment_dictionary_values(d: dict, i: int) -> dict:
    d = {k: v + i for k, v in d.items()}
    return d


class TestIncrementDictonaryValues(unittest.TestCase):

    def test_increment_dictonary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)


if __name__ == '__main__':
    unittest.main()