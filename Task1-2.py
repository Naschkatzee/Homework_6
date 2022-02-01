import argparse
import random 
import enum
from enum import Enum


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
 
print ('The toy is' , color.value + ' ' + toys.value)



