import Quandl

# TODO: demo ease of adding a missing package and a missing reference
today = datetime.today()

# get daily history of OIL on the National India Stock Exchange
data = Quandl.get('NSE/OIL')
print(data)
