import sys
from bs4 import BeautifulSoup
import requests


"""
The limitation of the programs are
- it will not capture any urls present outside the 'a' tags, for example paragraph with manually return url
- it will not capture the urls that doesn't contain an href with https:// or http:
"""

'''
function that checks the valid url
'''
def valid_url(string):
    # checking if the string contains the https:// or http://
    if 'http://' in string or 'https://' in string:
        return True
    else:
        return False

'''
Function to capture the external URLS and return the total number of external urls captured
'''
def capture_external_url(html_page):
    # list to store the external urls
    external_url_list = []
    # find all the a tags with href
    all_urls = html_page.find_all("a", href=True)
    for i in all_urls:
        if valid_url(i['href']):
            external_url_list.append(i)
    return len(external_url_list)

# capturing the second urls
# capturing more urs

'''
Capture the urls from the system arguments, with the help of beautifulsoup
'''
def run_scrapper(n):
    for i in range(1, n):
        # capture the url and return the results
        anticipated_url = sys.argv[i]
        # verify whether its a url or not
        if valid_url(anticipated_url):
            # capture the html page using bs4
            page = requests.get(anticipated_url)
            soup = BeautifulSoup(page.content, "html.parser")
            url_length = capture_external_url(soup)
            # print out to console
            print(str(sys.argv[i])+ " " + str(url_length))
        else:
            # else return invalid url
            print("URL is not a valid url", anticipated_url)


if __name__ == "__main__":
    # get the total number of url link present
    n = len(sys.argv)
    run_scrapper(n)