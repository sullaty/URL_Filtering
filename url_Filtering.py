#coding=utf-8

import sys
import os

def getUniqueURLs(input_file):
    unique_urls = set()

    with open(input_file, 'r') as f:
        for line in f:
            url = line.strip()
            if url:
                unique_urls.add(url)

    return list(unique_urls)

def saveUniqueURLs(unique_urls, output_file):
    with open(output_file, 'w') as f:
        for url in unique_urls:
            f.write(url + '\n')

def main():
    try:
        input_file = sys.argv[1].strip()
        output_file = sys.argv[2].strip()
    except Exception as e:
        print('error:', e)
        me = os.path.basename(__file__)
        print('usage: {} <input> <output>'.format(me))
        sys.exit()

    unique_urls = getUniqueURLs(input_file)
    saveUniqueURLs(unique_urls, output_file)

if __name__ == '__main__':
    main()

