import requests, bs4

# <!-- This is the example.html example file. -->
#
# <html><head><title>The Website Title</title></head>
# <body>
# <p>Download my <strong>Python</strong> book from <a href="http://
# inventwithpython.com">my website</a>.</p>
# <p class="slogan">Learn Python the easy way!</p>
# <p>By <span id="author">Al Sweigart</span></p>
# </body></html>

# making a beautiful soup parsing object from a file online
# res = requests.get('http://nostrach.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text)
# type(noStarchSoup)

# making a beautiful soup parsing object from a local html file
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')  # see above html example file to see what it is looking for
# elems                 -> [<span id="author">Al Sweigart</span>]
# elems[0].getText()    -> 'Al Sweigart'
# elems[0].attrs        -> {'id': 'author'}
