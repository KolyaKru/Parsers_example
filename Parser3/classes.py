from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
import requests

class Parse:
    def parsingcatalog(self, url):
        excel = Excel()

        params = {'page': 1}

        pages = 2

        while params['page'] <= pages:
            page = requests.get(url + str(params['page']))
            soup = BeautifulSoup(page.text, "html.parser")
            switch = soup.find_all('a', class_= "title-firm")
            for i in range(0, len(switch)):
                switchpage = requests.get("http://msk.all-gorod.ru/" + switch[i].get('href'))
                url_input = "http://msk.all-gorod.ru/" + switch[i].get('href')
                switchsoup = BeautifulSoup(switchpage.text, "html.parser")        
                titles = switchsoup.find('div', "firms-card frame-radius4").find('h1')
                addresses = switchsoup.find('div', class_= "address").find('strong') 
                tables = switchsoup.find('div', class_="main-firm-info")
                tels = switchsoup.find('div', class_="phone").find_all('strong')
                products = switchsoup.find('div', "activities company border-top").find_all('strong')

                for i in range(0, len(titles)):
                    title = titles.text
                    print(title)
                    address = addresses.text
                    print(address)
                    sites = tables.find('div', "www-site")
                    if (sites is None):
                        site = ""
                        print(site)
                    else:
                        site = sites.find('strong').text
                        print(site)
                    
                    phone = ""
                    for tel in tels:
                        phone += tel.text + ";"
                    print(phone)


                    prod = ""
                    products.pop(0)
                    for product in products:
                        prod += product.text + ";"
                    print (prod)
                    excel.AddExcel(title, title, "", address, phone, "", site, "", "", prod, url_input)
                    
            
            pagination = soup.find('div', class_="pagination").find_all('a')
            max_page = int((pagination[len(pagination)- 1].get('href')).replace("/rubrica/avtoaksessuary_-_proizvodstvo_prodazha/", ""))
            
            if (params['page'] == pages):
                params['page'] += 2
            
            if (pages <= max_page):
                if(params['page'] < pages):
                    pages = max_page
                    params['page'] +=1
                
                
         
class Excel:
    global wb

    wb = load_workbook('catalog2 27.08.2021.xlsx')

    global ws

    ws = wb.active

    def AddExcel(self, title, fulltitle, region, address, tel, email, url, contact, inn, product, url_input):

        ws.append([title, fulltitle, region, address, tel, email, url, contact, inn, product, url_input])      

    def SaveExcel(self):
        
        wb.save('catalog2 27.08.2021.xlsx')