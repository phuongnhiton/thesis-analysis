#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

# Read links from file
with open('liens.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Split content by newlines and remove empty entries
links = content.split('\n')[:-1]

# Verify we have the expected number of links
print(f"Total links: {len(links)}")

# Download thesis content for each link
thesis_id = 0
for link in links:
    # Construct the full URL
    url = "http://theses.fr" + link
    
    try:
        response = requests.get(url)
        print(f"Downloading: {url}")
        
        # Save thesis content to file
        with open(f"these{thesis_id}.txt", 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        thesis_id += 1
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

# Note: The following code is for parsing thesis metadata (commented out)
# To extract author information and thesis directors:
#
# for thesis_id in range(100):
#     with open(f'these{thesis_id}.txt', 'r', encoding='utf-8') as f:
#         content = f.read()
#
#     # Extract author
#     author_pattern = '<meta name="DC.creator" content=".*?">'
#     authors = re.findall(author_pattern, content, re.DOTALL)
#
#     # Extract thesis directors section
#     director_pattern = "<p>Sous la direction de .*?</p>"
#     director_section = re.findall(director_pattern, content, re.DOTALL)






