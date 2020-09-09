import requests                                  # to establish a connection with the website
from bs4 import BeautifulSoup	                   # to get the text value from the HTML code
import hashlib				             # to get the md5 hash value of the text

url = 'http://docker.hackthebox.eu:30312/'      # this is the url of the website

req = requests.session()        # this is for establishing the connection [syn], [syn, ack] and [ack]
out = req.get(url)              # out is the response code "<Response [200]>" in case of success
                                # but i want to get the HTML code to get the text value
                                # so i will work with out.text (HTML code of the web page)


soup = BeautifulSoup(out.text,'html.parser')    # here i passed HTML code to BeautifulSoup
                                                # to get soup object that enables me to search tags
                                                # and get the text value

tag = soup.find('h3')       # i used find method to search for tag 'h3'
                            # to get all tha tag '<h3 align="center">muds526wMisBMG4JUgyT</h3>'

             

hash_value = hashlib.md5(tag.text.encode()).hexdigest()     # we used 'tag.text' to get the text value of the tag
                                                            # 'muds526wMisBMG4JUgyT'
                                                            # and 'hashlib.md5' get the md5 hash value of the text

data = {'hash':hash_value}      # here i prepared the data to submit
                                # notice 'hash' is the name or id of the text box field
res = req.post(url, data)       # submit or post the request with the md5 hash value and get the response in 'res'
print(res.text)                 # display the response


