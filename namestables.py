import re
from functools import partial

from pluplusch import pluplusch

NAME = re.compile(r'.*(nom|name|last|first).*')
def filter_columns(catalogs = []):
    for dataset in pluplusch(catalogs = catalogs):
        colnames = list(filter(partial(re.match, NAME), dataset['colnames']))
        yield dataset['download_url'], colnames
