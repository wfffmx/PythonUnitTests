import datetime

symbol = input("Enter symbol: ")

if symbol.isalpha() == True and len(symbol) == 7 and symbol.isupper() == True:
    print("Valid selection")
else:
    print("Please enter a correct symbol")

try:
    chart_type = int(input("Enter chart type: "))
    if chart_type == 1 or chart_type == 2:
        print("Valid Chart Type")
    else:
        print("Please enter a correct chart type")
except ValueError:
    print("Please enter a correct chart type")

try:
    time_series = int(input("Enter time series: ")) 
    if time_series > 0 and time_series < 5:
        print("Valid time series") 
    else:
        print("Please enter a correct time series")
except ValueError:
    print("Invaild Time Series")
date_string = input("Enter start date in the format YYYY-MM-DD: ")
date_format = '%Y-%m-%d'

try:
    date_obj = datetime.datetime.strptime(date_string, date_format)
    print("Vaild date format")
except ValueError:
    print("Please enter start date in YYYY-MM-DD format")

date_string = input("Enter end date in the YYY-MM-DD format: ")
date_format = '%Y-%m-%d'

try:
    date_obj = datetime.datetime.strptime(date_string, date_format)
    print("Vaild date format")
except ValueError:
    print("Please enter end date in YYYY-MM-DD format")