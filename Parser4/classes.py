from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
import requests

class Parse:

    def parsingcatalog1(self, url):
        excel = Excel()
    
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        switch = soup.find_all('div', class_= "info-item")

        for i in range(0, len(switch)):
            switchpage = requests.get("http://psdir.ru/" + switch[i].find('h3').find('a').get('href'))
            url_input = "http://psdir.ru/" + switch[i].find('h3').find('a').get('href')
            print(url_input)
            switchsoup = BeautifulSoup(switchpage.text, "html.parser")  
            sites  = switchsoup.find('div', class_= "info").find(string = "Сайт:")
            emails  = switchsoup.find(string = "E-mail:")    
            titles = switchsoup.find('div', class_="company").find('h1')
            products  = switchsoup.find('div', class_= "info").find('a')
            addresses = switchsoup.find(string = "Адрес:")
            tels = switchsoup.find(string = "Телефоны:")
            regions = switchsoup.find(string = "Страна:")

            for i in range(0, len(titles)):
                title = titles.text
                print(title)
                product = products.text
                print(product)
                address = addresses.next_element
                print(address)
                tel = tels.next_element
                print(tel)
                region = (regions.next_element).replace(",","")
                print(region)

                if (sites is None):
                    site = ""
                    print(site)
                else:
                    site = sites.next_element
                    print(site)

                if (emails is None):
                    email = ""
                    print(email)
                else:
                    email = emails.next_element
                    print(email)
                excel.AddExcel(title, title, region, address, tel, email, site, "", "", product, url_input)

    def parsingcatalog(self, url):
        excel = Excel()

        params = {'page': 2}

        pages = 3

        while params['page'] <= pages:
            page = requests.get(url + "page/" + str(params['page']) + "/")
            soup = BeautifulSoup(page.text, "html.parser")
            switch = soup.find_all('div', class_= "info-item")
            for i in range(0, len(switch)):
                switchpage = requests.get("http://psdir.ru/" + switch[i].find('h3').find('a').get('href'))
                url_input = "http://psdir.ru/" + switch[i].find('h3').find('a').get('href')
                print(url_input)
                switchsoup = BeautifulSoup(switchpage.text, "html.parser")  
                sites  = switchsoup.find('div', class_= "info").find(string = "Сайт:")
                emails  = switchsoup.find('div', class_= "info").find(string = "E-mail:")    
                titles = switchsoup.find('div', class_="company").find('h1')
                products  = switchsoup.find('div', class_= "info").find('a')
                addresses = switchsoup.find(string = "Адрес:")
                tels = switchsoup.find(string = "Телефоны:")
                regions = switchsoup.find(string = "Страна:")

                for i in range(0, len(titles)):
                    title = titles.text
                    print(title)
                    product = products.text
                    print(product)
                    address = addresses.next_element
                    print(address)
                    tel = tels.next_element
                    print(tel)
                    region = (regions.next_element).replace(",","")
                    print(region)

                    if (sites is None):
                        site = ""
                        print(site)
                    else:
                        site = sites.next_element
                        print(site)

                    if (emails is None):
                        email = ""
                        print(email)
                    else:
                        email = emails.next_element
                        print(email)
                    excel.AddExcel(title, title, region, address, tel, email, site, "", "", product, url_input)

            if (soup.find(string ="следующая →") is not None):
                pages = int(soup.find('span', class_= "current").text) + 1
                params['page'] += 1
            else:
                params['page'] += 1           
            
class Excel:
    global wb

    wb = load_workbook('catalog3 27.08.2021.xlsx')

    global ws

    ws = wb.active

    def AddExcel(self, title, fulltitle, region, address, tel, email, url, contact, inn, product, url_input):

        ws.append([title, fulltitle, region, address, tel, email, url, contact, inn, product, url_input])      

    def SaveExcel(self):
        
        wb.save('catalog3 27.08.2021.xlsx')