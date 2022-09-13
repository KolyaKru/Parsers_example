

from classes import Parse, Excel
from bs4 import BeautifulSoup
import requests

parser = Parse()
excel = Excel()

urlq = "http://msk.all-gorod.ru/rubrica/avtoaksessuary_-_proizvodstvo_prodazha/"
parser.parsingcatalog(urlq)
excel.SaveExcel()
