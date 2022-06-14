import json
from unittest import TestCase, main

from task_16.exchanger.stas_task_4_hw_16 import start

'''The functionality of our module will be tested with two commands given to import: 
course usd course uah exchange usd 100 exchange uah 10000
STOP to proceed the code
and check how it will change values in our file, since testing closures is pretty damn hard'''


class TestExchange(TestCase):
    def setUp(self) -> None:
        with open('vault.txt') as json_file:  # Open our tested file within test module
            vault = json.load(json_file)
        try:  # Startin our main function
            start()
        except:  # Since we have exit() command it leads to stop test without checking anything, so need to pass for
            # moving forward
            pass

    def tearDown(self) -> None:  # This is required to set default values to our tested file for each iteration of test

        vault = {"currencies": [{"curr_id": 1, "curr_name": "USD", "curr_rate": 35.25, "curr_amount": 10000},
                                {"curr_id": 2, "curr_name": "UAH", "curr_rate": 35.15, "curr_amount": 100000.0}]}

        with open('vault.txt', 'w') as outfile:
            json.dump(vault, outfile)

    def test_vault(self):  # Testing if our values if equal to expected from entered commands
        with open('vault.txt') as json_file:
            vault = json.load(json_file)
        assert vault == {
            "currencies": [{"curr_id": 1, "curr_name": "USD", "curr_rate": 35.25, "curr_amount": 9816.312056737588},
                           {"curr_id": 2, "curr_name": "UAH", "curr_rate": 35.15, "curr_amount": 106485.0}]}


if __name__ == "__main__":
    main()
