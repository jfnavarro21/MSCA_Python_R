# Task 4b: Count the words

# Alot of this code is from
# http://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text

import urllib.request # gets the information from a web page
from bs4 import BeautifulSoup # takes html and turns into bs object you can manipulate
import re # regular expressions is used to identify patterns

# reads the stackoverflow website and stores its html data into variable html
html = urllib.request.urlopen('http://www.stackoverflow.com').read()
# creating a beautiful soup object that still looks like html (has tags, etc)
soup = BeautifulSoup(html, 'html.parser')
# uses findAll texts to create a list of the texts of the page
texts = soup.findAll(text=True)

# Create a function that gets rid of style, script etc tags also uses regular expressions to clean the texts
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

#use the filter function to run visible on texts
visible_texts = filter(visible, texts)
# make visible_texts a list
l_visible_texts = list(visible_texts)
# use ''.join to join all the elements in the list
j_visible_texts = ''.join(l_visible_texts)
# use .split() to split the items and put back into a list
final_visible_texts = j_visible_texts.split()
# get the length of the list
print(len(final_visible_texts))

# Output:
#C:\Users\JohntheGreat\Anaconda3\python.exe C:/Users/JohntheGreat/Documents/MSCA/Python3forStreamingAnalytics/Week4/Assignment4_Task4B.py
#2876

#Process finished with exit code 0

