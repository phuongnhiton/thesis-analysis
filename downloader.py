#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import pickle
import csv

# Thesis search parameters
list_ids = []
request_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6'
}

# URL for searching theses from 1965 to 2019 in "Lettres modernes" discipline
url = "http://theses.fr/fr/?q=&fq=dateSoutenance:[1965-01-01T23:59:59Z%2BTO%2B2019-12-31T23:59:59Z]&checkedfacets=discipline=Lettres%20modernes"

try:
    response = requests.get(url, headers=request_headers, timeout=10)
    print(f"HTTP Status Code: {response.status_code}")
    
    content = response.text
    
    # Save response to file for debugging (optional)
    # with open('thesis_source.txt', 'w', encoding='utf8') as output:
    #     output.write('%r' % content)
    
    # Extract thesis identifiers using regex
    # identifier_pattern = "<a href=/2018TOUR2019>((.+?(?=</a>)))"
    # thesis_ids = re.findall(identifier_pattern, content)
    # print(f"Thesis IDs: {thesis_ids}")
    
except requests.RequestException as e:
    print(f"Error fetching URL: {e}")
