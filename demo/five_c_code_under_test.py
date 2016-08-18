# TODO: Demo vertical window partitioning, unit test framework integration, and coverage.
# TODO: Show staticmethod to function and back.
# TODO: Select expiry_date and show scrollbar
# TODO: Show the integrated Python Console.

import calendar
from datetime import datetime


class FuturesContract:

    def __init__(self):
        pass

    @staticmethod
    def get_cme_quarterly_forward_month_string(as_of_datetime=datetime.today()):
        return FuturesContract.get_cme_quarterly_forward_month(as_of_datetime).strftime("%Y%m%d")

    @staticmethod
    def get_cme_year_number(as_of=datetime.today()):
        result = str(as_of.year % 10)
        if as_of.month == 12:
            first_thursday = calendar.Calendar(3).monthdatescalendar(as_of.year, as_of.month)[1][0]
            if first_thursday < as_of.date() or (first_thursday == as_of.date() and as_of.time().hour >= 5):
                result = str((as_of.year + 1) % 10)
        return result

    @staticmethod
    def get_cme_quarterly_forward_month(as_of_datetime=datetime.today()):
        first_thursday = None
        expiry_date = datetime(1900, 01, 01)
        # calendar.Calendar(x).monthdatescalendar(year, month)[n][0]
        if as_of_datetime.month in (1, 2):
            expiry_date = calendar.Calendar(4).monthdatescalendar(as_of_datetime.year, 3)[3][0]
        elif as_of_datetime.month in (4, 5):
            expiry_date = calendar.Calendar(4).monthdatescalendar(as_of_datetime.year, 6)[3][0]
        elif as_of_datetime.month in (7, 8):
            expiry_date = calendar.Calendar(4).monthdatescalendar(as_of_datetime.year, 9)[3][0]
        elif as_of_datetime.month in (10, 11):
            expiry_date = calendar.Calendar(4).monthdatescalendar(as_of_datetime.year, 12)[3][0]
        elif as_of_datetime.month in (3, 6, 9):
            first_thursday = calendar.Calendar(3).monthdatescalendar(as_of_datetime.year, as_of_datetime.month)[1][0]
            if first_thursday > as_of_datetime.date() or (
                    first_thursday == as_of_datetime.date() and as_of_datetime.time().hour < 17):
                expiry_date = calendar.Calendar(4).monthdatescalendar(as_of_datetime.year, as_of_datetime.month)[3][0]
            else:
                expiry_date = calendar.Calendar(4).monthdatescalendar(as_of_datetime.year, as_of_datetime.month + 3)[3][0]
        elif as_of_datetime.month == 12:
            first_thursday = calendar.Calendar(3).monthdatescalendar(as_of_datetime.year, 12)[1][0]
            if first_thursday > as_of_datetime.date() or (
                    first_thursday == as_of_datetime.date() and as_of_datetime.time().hour < 17):
                expiry_date = calendar.Calendar(4).monthdatescalendar(as_of_datetime.year, 12)[3][0]
            else:
                expiry_date = calendar.Calendar(4).monthdatescalendar(as_of_datetime.year - 1, 3)[3][0]
        return expiry_date