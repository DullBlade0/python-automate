import requests, bs4, os

#def requestGallery():
    
searchTerm = input('Insert term to search: ')
os.makedirs('imgur/'+searchTerm, exist_ok=True)
os.chdir('imgur')
print(os.getcwd())
link = 'http://imgur.com/search?q='+searchTerm
print('Searching images...')
res = requests.get(link)
res.raise_for_status()
imgurSoup = bs4.BeautifulSoup(res.text, "lxml")
searchResults = imgurSoup.select('div > .post > .image-list-link')


#From here I have all the links for the images in the search.
for item in searchResults:
    item = item.get('href') #This is so I can access the gallery.
    galleryUrl = 'http://imgur.com'+item #Link to view the image.
    print('Downloading page %s...' % galleryUrl)
    res = requests.get(galleryUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    
    
    #At this point I'm inside the link of the first image of the search result.
    #galleryElems = soup.select('div > .zoom > .post-image-placeholder') #This should be picking the tags to grab the src.
    galleryElems = soup.find_all('div', class_='post-image-placeholder')
    print('The gallery elements are:')
    print(galleryElems)
    
    
    
    #Get src for all images. 
    '''for galleryItem in galleryElems:
        galleryItem = galleryItem.get('src')
        #galleryItem = galleryItem.find_all('src')    
        print(galleryItem) 
        imageUrl = 'http:'+galleryItem
        print('Downloading image from %s...'% imageUrl)
        res = requests.get(imageUrl)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "lxml")
        imgElem = soup.select('img')
        print('Saving image...%s' % imageUrl)
        imageFile = open(os.path.join(searchTerm, os.path.basename(imageUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close'''
