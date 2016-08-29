import requests, bs4, os

searchTerm = input('Insert a search term: ')
url = http://imgur.com/t/ + searchTerm
os.makedir(searchTerm, exist_ok=True)
while not url.endswith(''):   #Tentative
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, "lxml")

	#Find the image
	imageElem = soup.select('')
	if imageElem == []:
		print('There\'s no image.')
	else:
		try:
			imageUrl =  'http:' + imageElem[0].get('src')
			print('Downloading image %s...' % (imageUrl))
			res = requests.get(imageUrl)
			res.raise_for_status
		except:
			prevLink = soup.select('')[0]
			url = '' + prevlink			
			continue						#inside > div.left.post-pad > div.post-container > div.post-header > div > div.next-prev > div.btn.btn-action.navNext
		imageFile = open(os.path.join(searchTerm, os.path.basename()),'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
	prevLink = soup.select()[0]
	url = url + '/' + prevLink.get('href')
print('Done.')