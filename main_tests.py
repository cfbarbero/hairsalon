import lib2to3.tests.data.py2_test_grammar

import main

class CustomerBuilderTests:
    def test_when_no_mins_until_next_customer_creates_customer(self):
        builder = main.CustomerBuilder()
        builder.mins_until_next_customer=0
        assert builder.try_get_new_customer() not None