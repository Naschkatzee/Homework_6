import argparse
from pathlib import Path
from random import randint
import pathlib
from loguru import logger
import logging
import os

logger.add ('debug.log', format = '{time} {level} {message}', level = 'DEBUG')

#Path ('main').mkdir (exist_ok = True)
#for i in range (10):
#    Path ( f'main/'
#        f'{randint (2020,2022)}-'
#       f'{randint (1,12)}-'
#       f'{randint (1,31)}.txt').touch ()

parser = argparse.ArgumentParser()
parser.add_argument('division', help = 'Разделитель в названии', type = str)

args = parser.parse_args()

division = args.division

@logger.catch
def name ():
    path = '.\main'
    list_of_files = list(sorted(os.listdir(path)))
    print(list_of_files)
    for file in list_of_files:
        fold1 = (file.split('-')[0])
        fold2 = (file.split('-')[1])
        fl = (file.split('-')[2])
        Path(f'main/{fold1}/{fold2}/').mkdir(parents=True, exist_ok=True)
        path1 = f'.\main/{file}'
        path2 = f'.\main/{fold1}/{fold2}/{fl}'

        os.replace(path1, path2)

name ()


import logging

logger = logging.getLogger()
handler = logging.FileHandler('logs.log')
logger.addHandler(handler)
logger.error('Our Third Log Message')



