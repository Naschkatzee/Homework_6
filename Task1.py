import argparse
from datetime import datetime, date, time


parser = argparse.ArgumentParser()
parser.add_argument('years', help = 'Новый год', type = int)
parser.add_argument('hours', help = 'Часов сейчас', type = int)

args = parser.parse_args()

years = args.years
hours = args.hours

# now = datetime.now()
today = date.today()
# current_hour = datetime.now().hour
new_year_date = date(years, 12, 31)
time_to_ny = new_year_date - today
a = 24 - hours  # current_hour
print(f'New year is {time_to_ny.days} days and {a} hours away')



