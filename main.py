#!/usr/bin/env python
#! -*- coding: utf-8 -*-


import sys
import threading
from scripts.crawler import WebCrawler
from scripts.workingp import ParseUrl


# for debug purposes
filename = [
        'http://localhost/pagina.html',
        'http://localhost/pagine2.html',
        'http://google.com.br/search?q=',
        'https://duckduckgo.com/html'
]


def read_file(filename):
    list_of_urls = []
    file_list = open(filename, 'r')
    url_list = file_list.readlines()

    for line in url_list:
        list_of_urls.append(line)
    return list_of_urls


def load_urls(filename):
    url_lst = []
    for url in filename:
        url_lst.append(url)
    return url_lst


def process_website_by_id(website_id):
    print('Processing website-id: %s' % website_id)


def main_loop():

    # reading from DB.
    use_debug = False
    # FILE_DATABASE = '/tmp/list_of_urls.txt)'
    FILE_DATABASE = sys.argv[1]

    for id, url in enumerate(ParseUrl.process_from_file(FILE_DATABASE)):
        print('%d| Translated: %s' % (id ,url))
    user_input_id = int(input('> Enter the website id: '))
    process_website_by_id(user_input_id)

    """
    # main loop/processing urls
    while True:

        # reading from file/csv/database
        if use_debug:
            print(type(read_file('/tmp/list_of_urls.txt')))
        
        for url in read_file(FILE_DATABASE):
            print('URL: %s' % url)

        # process the main thread
        for webpage in load_urls(filename):
            print('Processing webpage %s' % webpage)
    """


def main():
    main_loop()


if __name__ == '__main__':
    main()


