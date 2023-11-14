import urllib.request, urllib.error, urllib.parse
import sys

# Attempt to get some debugging
DEBUG = False

# Use with the command line: i.e. python3 single_page.py "google.com/example"
url = sys.argv[1]

# Catch the data
response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

# We use the ending of files to name the page
file_name = url.split("/")[-1]

if DEBUG:
    print(file_name)
    print(url)
else:
    with open(f"./test_pages/{file_name}.html", "w+") as my_file:
        my_file.write(webContent)