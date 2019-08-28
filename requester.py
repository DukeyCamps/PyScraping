import requests, bs4, re
import os
from time import sleep

curDir = os.getcwd()
if not os.path.exists(curDir + '/books'):
	os.mkdir('books')   








titleMatch = re.compile(r'START OF THIS PROJECT GUTENBERG EBOOK.*[*]')
title = None
folder = './books/'


def ext_title(text):
    return ''.join(titleMatch.findall(text))[38:-4]


def book_address(book_ID):
    return 'https://www.gutenberg.org/files/{0}/{0}-0.txt'.format(book_ID)


def request_download(ID):
    global title
    address = book_address(ID)
    res = requests.get(address)    
    title = ext_title(res.text)
    title = title.lower()
    
    if len(title) > 1:   
        newFile = open(folder + title, 'wb')
        for line in res.iter_content(100000):
            newFile.write(line)
        
        newFile.close()
        print('wrote a book:', book_address(ID), title)
