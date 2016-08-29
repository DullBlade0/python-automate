import requests, bs4, os

searchTerm = input('Insert term to search: ')
os.makedirs('imgur/'+searchTerm, exist_ok=True)
os.chdir('imgur')
print(os.getcwd())
link = 'http://imgur.com/search/score/all?q_type=jpg&q_all='+searchTerm
print('Searching images...')
res = requests.get(link)
res.raise_for_status()
imgurSoup = bs4.BeautifulSoup(res.text, "lxml")
#elems = imgurSoup.select('div > .post > a > .image-list-link')

#Selects object with img tag on the page.
elems = imgurSoup.select('img')
#From here I have all the links for the images in the search.


#Does this action for all the items in the cycle.
for item in elems:
    item = item.get('src') #Gets the src tag info. At this point I'm on the image itself.
    if not item.endswith('.jpg'):
        continue
    imageUrl = 'http:'+item
    print('Downloading image from %s...' % item)
    res = requests.get(imageUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    imgElem = soup.select('img')
    print('Saving image...')
    print(imageUrl)
    imageFile = open(os.path.join(searchTerm, os.path.basename(imageUrl)), 'wb') 
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close

            
