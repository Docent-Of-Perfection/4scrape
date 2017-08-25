#python3
import sys, bs4, requests, os


def debug(dbug):
	print(dbug)

if len(sys.argv) > 1:
	specifiedBoard = sys.argv[1]
else:
		print("Specify board letter")
		specifiedBoard = input()

urlFull = "http://4chan.org/" + specifiedBoard

debug("The urlFull variable value is " + urlFull)

markup = requests.get(urlFull)
markup.raise_for_status()

searchableMarkup = bs4.BeautifulSoup(markup.text,"lxml")
#markupText = markup.text

#print(markup.url)

# 1. Pull all image tags from HTML (DONE)
allImages = searchableMarkup.select('img')
#print(allImages)
#print(allImages[0])

# 2. Filter out ads/banners(identify class/markup unique to unwanted images)

#3. Check for existing scrape directory and create one if necessary to store files
folder = os.path.expanduser('~/Pictures')

#This line returns only immediate child folders of the 'Pictures' folder
dir_list = next(os.walk(folder))[1]
if '4scrape' not in str(dir_list):
	try:
		#creates a folder called '4scrape' in the Pictures directory
		os.mkdir(folder + '/4scrape')
		print("Creating directory")
	except:
		print("Directory already exists")
print("This is a list of the directories under 'Pictures' " + str(dir_list))
#4. Write images to disk

#get the URl for each image pulled from the requested board
for image in allImages:
#the [2:] removes the // that prepends image files on 4chan's web server
	print(image.get('src')[2:]) 


