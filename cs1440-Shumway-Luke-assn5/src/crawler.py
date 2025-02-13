#!/usr/bin/python3


# pip install --user requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import sys
import time


def crawl(url, depth, maxdepth, visited):
    """
    Given an absolute URL, print each hyperlink found within the document.

    Your task is to make this into a recursive function that follows hyperlinks
    until one of two base cases are reached:

    0) No new, unvisited links are found
    1) The maximum depth of recursion is reached
    """
    if depth > maxdepth:
        return
    else:
        # Add unique URLs to the visited list
        visited.add(url)
        for i in range(depth):
            print("    ", end="")
        print(url)
    try:
        response = requests.get(url)
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return

        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
        for a in links:
            link = a.get('href')
            # Only deal with resources accessible over HTTP or HTTPS
            if link and link.startswith('http'):
                # Create an absolute address from a (possibly) relative URL
                absoluteURL = urljoin(url, link.split("#")[0])
                if absoluteURL not in visited:
                    crawl(absoluteURL, depth + 1, maxdepth, visited)
    except Exception:
        print("An Error occurred:  Returning to previous page")
        return

    return


# An absolute URL is required to begin
if len(sys.argv) < 2:
    print("Error: no Absolute URL supplied")
    sys.exit(1)
elif len(sys.argv) < 3:
    url = sys.argv[1]
    maxDepth = 3
else:
    url = sys.argv[1]
    try:
        if int(sys.argv[2]) >= 0:
            maxDepth = int(sys.argv[2])
        else:
            print("Error: Invalid depth level supplied")
            print("Please supply a positive, whole number for the depth level")
            sys.exit(1)
    except ValueError:
        print("Error: Invalid depth level supplied")
        print("Please supply a positive, whole number for the depth level")
        sys.exit(1)

parsed = urlparse(url)
if parsed.scheme and parsed.netloc:
    start = time.time()
    visited = set()
    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")
    try:
        crawl(url, 0, maxDepth, visited)
        end = time.time()
        plural = 's' if len(visited) != 1 else ''
        print(f"Visited {len(visited)} unique page{plural} in {round(end - start, 4)} seconds")

    except KeyboardInterrupt:
        end = time.time()
        plural = 's' if len(visited) != 1 else ''
        print(f"Visited {len(visited)} unique page{plural} in {round(end - start, 4)} seconds")
        print("Goodbye")
else:
    print("Error: Invalid URL supplied")
    print("Please supply an absolute URL to this program")
