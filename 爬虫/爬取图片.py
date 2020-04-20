from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
import os

url = 'https://www.yinkuan.club/index_photo.html'
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all('img')
print(img)

os.makedirs('./luvv/', exist_ok=True)

main_url = 'https://www.yinkuan.club/'
for yk in img:
    img_url = yk['src']
    img_name = img_url.split('/')[-1]

    print(img_name)

    real_url = main_url + img_url
    urlretrieve(real_url, './luvv/%s' % img_name)
