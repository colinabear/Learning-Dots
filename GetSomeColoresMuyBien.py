from bs4 import BeautifulSoup
import requests
import urllib.request

url = 'https://www.colorhexa.com/color-names'

# Dict to hold all of the name/RGB references
big_dict = {}

# List to sort all of the RGB integer values
big_list = []

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Takes an RGB value and converts it to its integer value
def get_numerical(rgb):
    nums = rgb.split()
    return int(nums[0]) * 255 * 255 + int(nums[1]) * 255 + int(nums[2])

def get_RGB(num):
    r = num%255*255*255
    g = num%255
    b = num

# To download the whole data set, let's do a for loop through all a tags
for tr in soup.findAll('tr'):
    if tr.findAll('td') == []:
        continue
    color_name = tr.findAll('td')[0].getText()
    rgb_code = tr.findAll('td')[2].getText() + " " + tr.findAll('td')[3].getText() + " " + tr.findAll('td')[4].getText()
    big_dict[rgb_code] = color_name


x = 242*255*255 + 251*255 + 21

while x > 1:
    if x >

#print(big_dict)