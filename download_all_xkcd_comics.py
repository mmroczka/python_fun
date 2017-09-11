#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True) # store comic in folder xkcd, make it if it doesn't exist
while not url.endswith('#'):
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    parser = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image.
    comic_html = parser.select('#comic img')
    if comic_html == []:
        print('Could not find comic at {}'.format(url))
    else:
        # TODO: Download the image.
        comic_url = 'http:' + comic_html[0].get('src')
        print('Downloading comic at {}'.format(comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    # TODO: Save the image to ./xkcd.
    comic = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for bytes in res.iter_content(100000):
        comic.write(bytes)
    comic.close()
    # TODO: Get the Prev button's url.
    prevLink = parser.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done')
