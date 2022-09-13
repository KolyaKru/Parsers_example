from classes import Parse, Excel
from bs4 import BeautifulSoup
import requests

parser = Parse()
excel = Excel()

urlq = "http://psdir.ru/category/list/8/"
parser.parsingcatalog1(urlq)
excel.SaveExcel()

parser.parsingcatalog(urlq)
excel.SaveExcel()

