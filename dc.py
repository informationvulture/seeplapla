import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import time


# Main course list
url = "https://www.douglascollege.ca/courses"

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

# Get all the divs which have the URL tag
soup = BeautifulSoup(webContent, 'html.parser')
divs = soup.find_all('div', class_='field-content')

# This gets the URL tag, which has the endpoint for each course category
course_names = []
for div in divs:
    a_tag = div.find('a')
    if a_tag and a_tag.has_attr('href'):
        course_names.append(a_tag['href'].split("/")[-1])

# Do the actual work
for course in course_names[0:3]: # To use in production remove '[0:3]'
    url = f"https://www.douglascollege.ca/courses/{course}"

    response = urllib.request.urlopen(url)
    webContent = response.read().decode('UTF-8')

    # Get the actual course names
    soup = BeautifulSoup(webContent, 'html.parser')
    td_tags = soup.find_all('td', {'headers': 'view-field-course-code-table-column', 'class': 'views-field views-field-field-course-code'})
    
    # Some weird padding on the right needs to be removed
    courses = [tag.get_text().rstrip() for tag in td_tags]

    # Minimum course number
    min_course = courses[0].split(' ')[-1]

    # Maximum course number
    max_course = courses[-1].split(' ')[-1]

    # Are all courses the same beginning name?
    sig_code = len(set([course.split(" ")[0] for course in courses])) == 1

    print("**************")
    print(f"{course} has these:")
    print(courses)
    print("*** Stats: ***")
    print(f"Count: {len(courses)}")
    print(f"Single Code: {sig_code}")
    print(f"Min #: {min_course}")
    print(f"Max #: {max_course}")
    print("**************")

    # Make it less weird for the web masters
    time.sleep(3)

