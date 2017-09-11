import requests

# here is a simple get request to download the file
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

# simple way to check status code is ok
res.status_code == requests.codes.ok

# but an even easier way is to just use the raise for status function
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

name_of_file = 'RomeoAndJuliet.txt'
create_new_file_and_write_in_binary = 'wb'

playFile = open(name_of_file, create_new_file_and_write_in_binary)

num_bytes = 100000
for chunk in res.iter_content(num_bytes):
    playFile.write(chunk)

playFile.close()
