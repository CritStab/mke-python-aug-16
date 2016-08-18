import datetime
import pandas_datareader.data as web

# TODO: Demo 1) Evaluate Expression, 2) View Dataframe, 3) Step into pandas.

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 8, 6)

# Download Payrolls and Unemployment Rate data from St. Louis Federal Reserve.
payroll_unemployment = web.get_data_fred(["PAYEMS", "UNRATE"], start, end)

print(payroll_unemployment.tail())