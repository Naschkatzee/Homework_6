import argparse
import random 
import enum
from enum import Enum
from loguru import logger
import logging

logger.add ('debug.log', format = '{time} {level} {message}', level = 'DEBUG')


parser = argparse.ArgumentParser()
parser.add_argument('--color', help = 'Цвета', type = str)
parser.add_argument('--toys', help = 'Игрушки', type = str)

args = parser.parse_args()


class Color (Enum):
    color = args.color
    #a = 'red'
    #b = 'blue'
 
color = random.choice (list(Color))


class Toys (Enum):
    toys = args.toys
    #c = 'angel'
    #d = 'ball'

toys = random.choice (list(Toys))
 
@logger.catch
def main ():
    print ('The toy is' , color.value + ' ' + toys.value)

main ()

import logging

logger = logging.getLogger()
handler = logging.FileHandler('logs.log')
logger.addHandler(handler)
logger.error('Our Second Log Message')


