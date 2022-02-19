import argparse
from datetime import datetime, date, time
from loguru import logger
import logging

logger.add ('debug.log', format = '{time} {level} {message}', level = 'DEBUG')


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

@logger.catch
def main ():
    print(f'New year is {time_to_ny.days} days and {a} hours away')

main ()

import logging

logger = logging.getLogger()
handler = logging.FileHandler('logs.log')
logger.addHandler(handler)
logger.error('Our First Log Message')



