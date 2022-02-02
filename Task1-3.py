import argparse
from pathlib import Path
from random import randint
import pathlib

#Path (r'C:/Users/Tatsiana/Homework_6/main.py').mkdir (exist_ok = True)
#for i in range (10):
#    Path ( f'main.py/'
#        f'{randint (2020,2022)}-'
#       f'{randint (1,12)}-'
#       f'{randint (1,31)}.txt').touch ()

parser = argparse.ArgumentParser()
parser.add_argument('division', help = 'Разделитель в названии', type = str)

args = parser.parse_args()

division = args.division


contents = pathlib.Path('main.py').iterdir()
for path in contents:
  if path.is_file ():
     pathlib.Path.rename = path.stem.replace('-', division) + path.suffix
     print (pathlib.Path.rename)







