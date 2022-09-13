from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests

class Parse:
    
    def parsingAkum(self, url):
        excel = Excel()
        page = requests.get(url)

        soup = BeautifulSoup(page.text, "html.parser")
        amperagefull = soup.find('div', class_='description-item__text').find('li')
        amperagepart = soup.find('div', class_='description-item__text').find('li').find('span')

        price = soup.find('div', class_= 'description-item__basket-subprice')
        title = soup.find('h1')

        if (amperagefull is not None and amperagepart is not None and price is not None):
            amperage = amperagefull.text.replace(amperagepart.text, "")
            excel.AddExcel(title.text, url, price.text, amperage)

class Excel:
    global wb

    wb = Workbook()

    global ws

    ws = wb.active

    def AddExcel(self, title, url, price, amperage):

        ws.append([title, url, price, amperage])      

    def CreateExcel(self):

        ws.append(["Название", "Сайт", "Цена", "Пусковой ток"])

    def SaveExcel(self):
        
        wb.save('sample.xlsx')
        
        
    
    