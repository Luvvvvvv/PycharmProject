from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlwt

url = 'http://www.gaosan.com/gaokao/259180.html'
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')

table = soup.find('table')
tbody = table.find('tbody')

tr = tbody.find_all('tr')
row = 1
for l in tr:
    td = l.find_all('td')
    xh = td[0].get_text()
    mc = td[1].get_text()
    jg = td[2].get_text()
    worksheet.write(row, 1, xh)
    worksheet.write(row, 2, mc)
    worksheet.write(row, 3, jg)
    row = row + 1

workbook.save('luv.xls')
