import requests, bs4
import re
from time import sleep
import warnings
import requester


warnings.filterwarnings('ignore')

res = requests.get('http://www.gutenberg.org/browse/scores/top')
bookNumReg = re.compile(r'\d+["$]')

example_supper = bs4.BeautifulSoup(res.text)

def gen_ID():

    for line in example_supper.select('li'):
        for crap in line:
            if 'ebooks' in str(crap):
                ID = ''.join(bookNumReg.findall(str(crap)))[:-1]
                yield ID
            

IDMAKER = gen_ID() 
