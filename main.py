import os
import requests
import xml.dom.minidom

dl_foler = 'downloaded'
os.makedirs('downloaded', exist_ok=True)

dl_url = 'https://podcast.ucsd.edu/watch/wi20/cse20_b00'

data = requests.get('https://podcast.ucsd.edu/Podcasts/rss.aspx?podcastId=6621&v=1').content
doc = xml.dom.minidom.parseString(data)

for item in doc.getElementsByTagName('link'): 
    link = item.childNodes[0].toprettyxml().strip() 
    name = link.rsplit('/', 1)[-1] 
    print('downloading:', name) 
    response = requests.get(link) 
    with open(os.path.join(dl_foler, name), 'wb') as f: 
        f.write(response.content)