from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
import requests

class Parse:
    def parsingcatalog1(self, url):
        excel = Excel()

        params = {'page': 2}
        
        pages = 3

        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        
        titles = soup.find_all('span', class_="h2")
        regions = soup.find_all(string = "Страна:")
        tels = soup.find_all(string = "Телефон:")
        tables = soup.find_all('table', class_= "comp-data-table")
        products = soup.find_all('div', class_="mini-centr-block")

        for i in range(0, len(titles)):
            title = titles[i].text
            region = regions[i].next_element.text
            tel = tels[i].next_element.text

            print(title)
            print(region)
            print(tel)
            urls = tables[i].find(string = "Сайт:")
            adresses = tables[i].find(string = "Адрес:")

            if (urls is None):
                urlq = ""
                print(urlq)
            else:
                urlq = urls.next_element.text
                print(urlq)

            if (adresses is None):
                adress = ""
                print(adress)
            else:
                adress = adresses.next_element.text
                print(adress)

            product = products[i].next_element.text
            url_input = titles[i].next_element.get('href')
            print(product)
            print(url_input)  
            excel.AddExcel(title, title, region, adress, tel,"", urlq, "", "", product, url_input)

    def parsingcatalog(self, url):
        excel = Excel()

        params = {'page': 2}
        
        pages = 3

        while params['page'] <= pages:

            page = requests.get(url, params=params)
            soup = BeautifulSoup(page.text, "html.parser")
        
            titles = soup.find_all('span', class_="h2")
            regions = soup.find_all(string = "Страна:")
            tels = soup.find_all(string = "Телефон:")
            tables = soup.find_all('table', class_= "comp-data-table")
            products = soup.find_all('div', class_="mini-centr-block")

            for i in range(0, len(titles)):
                title = titles[i].text
                region = regions[i].next_element.text
                tel = tels[i].next_element.text

                print(title)
                print(region)
                print(tel)
                urls = tables[i].find(string = "Сайт:")
                addresses = tables[i].find(string = "Адрес:")

                if (urls is None):
                    urlq = ""
                    print(urlq)
                else:
                    urlq = urls.next_element.text
                    print(urlq)

                if (addresses is None):
                    address = ""
                    print(address)
                else:
                    address = addresses.next_element.text
                    print(address)

                product = products[i].next_element.text
                url_input = titles[i].next_element.get('href')
                print(product)
                print(url_input)  
                excel.AddExcel(title, title, region, address, tel,"", urlq, "", "", product, url_input)

            
            if (soup.find('li', class_= "next disabled") is None):
                last_page = int(soup.find('li', class_= "next").next_element.get('data-page')) + 1
                pages = last_page if pages < last_page else pages
                params['page'] += 1 
            elif(soup.find('li', class_= "next disabled") is not None):
                params['page'] +=1
                   
class Excel:
    global wb

    wb = load_workbook('catalog.xlsx')

    global ws

    ws = wb.active

    def AddExcel(self, title, fulltitle, region, adress, tel, email, url, contact, inn, product, url_input):

        ws.append([title, fulltitle, region, adress, tel, email, url, contact, inn, product, url_input])      

    def SaveExcel(self):
        
        wb.save('catalog.xlsx')