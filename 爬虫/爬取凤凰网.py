from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlwt

url = 'https://www.ifeng.com/'
html = urlopen(url).read().decode('utf-8')
bs = BeautifulSoup(html, 'lxml')

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('凤凰网新闻')

body = bs.find('body')
news = body.find_all('a')
row = 1

for l in news:
    if l:
        if l.text and len(l.text) > 6:
            news = l.get_text()
            address = l.get('href')
            worksheet.write(row, 0, news)
            worksheet.write(row, 1, address)
            row = row + 1
            workbook.save('news.xls')
