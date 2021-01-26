import unittest 
from utils.errors import ElementIsNotTypeInt, ArgumentIsNotTypeList, MissingSellPrice


def loss_calculator(pricesLst: list) -> int:
    """
    Takes long list of prices, each element pair contains a buy and a sell price, 
    compares buy and sell and calculate highest loss

    note - unsure if I have misinterpreted the task, apologies if I have :(

    :param pricesLst: list consisting of buy and sell prices
    :type pricesLst: list
    :raises ArgumentIsNotTypeList: error occurs when pricesLst is not of type list
    :raises ElementIsNotTypeInt: error occurs when element in pricesLst is not of type list
    :raises MissingSellPrice: error occurs when pricesLst is odd e.g. not divisible by  
    :return: highest loss between buy and sell
    :rtype: int
    """

    # Type checking data as python is not a statically typed 
    if not isinstance(pricesLst, list):
        raise ArgumentIsNotTypeList("pricesLst is of type {} not list".format(pricesLst))

    # Type checking each element in array, Potential issue depending on size of dataset  
    elif not all(isinstance(x, int) for x in pricesLst):
        raise ElementIsNotTypeInt("element in pricesLst is not int")

    # If list is not divisible by 2 means that it is not even meaning we can assume a sell price is missing
    elif not len(pricesLst) % 2 == 0:
        raise MissingSellPrice("pricesLst is missing a sell price")

    # Actual "solution" 
    
    seperated_pricesLst = [pricesLst[i:i + 2] for i in range(0, len(pricesLst), 2)]
    all_losses = list(map(lambda buy_sell: buy_sell[1] - buy_sell[0], seperated_pricesLst))

    return sorted(all_losses)[0]
  


class TestLossCalculator(unittest.TestCase):

    def test_loss_calculator(self):
        test_data = [2, 1, 10, 1, 200, 100]
        result = loss_calculator(test_data)
        self.assertEqual(-100, result)

    def test_loss_calculator_wrong_type(self):
        test_data = 0
        # lambda is used due to ArgumentIsNotTypeList getting rasied before self.assertRaises is called
        # the alternative way would be to call the function like this -> self.assertRaises(ArgumentIsNotTypeList, loss_calculator, test_data)
        self.assertRaises(ArgumentIsNotTypeList, lambda: loss_calculator(test_data))

    def test_loss_calculator_wrong_type_in_list(self):
        test_data = [2, 1, 10, 1, 200, "a"]
        self.assertRaises(ElementIsNotTypeInt, lambda: loss_calculator(test_data))

    def test_loss_calculator_un_even_list(self):
        test_data = [2, 1, 10, 1, 200]
        self.assertRaises(MissingSellPrice, lambda: loss_calculator(test_data))


if __name__ == '__main__':
    unittest.main()