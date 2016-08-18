from nose.tools import assert_equal
from nose_parameterized import parameterized
from datetime import datetime
import inspect

from five_c_code_under_test import FuturesContract


## nosetests -s test/security/instrument_tests.py

class TestFuturesContractClass:
    @parameterized.expand([
        ('20151218', datetime(2015, 11, 1)),
        ('20151218', datetime(2015, 12, 1)),
        ('20160318', datetime(2015, 12, 15)),
        ('20160318', datetime(2016, 1, 1)),
        ('20160318', datetime(2016, 1, 10)),
        ('20160916', datetime.today())  # this will break...eventually.
    ])
    def test_get_forward_month_year_string(self, expected, as_of_date):
        assert_equal(expected, FuturesContract.get_cme_quarterly_forward_month_string(as_of_date))
