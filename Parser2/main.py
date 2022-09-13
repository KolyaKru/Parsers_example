from classes import Parse, Excel
from bs4 import BeautifulSoup
import requests

parser = Parse()
excel = Excel()

urlq = "https://www.oborudunion.ru/company/transportnaya-tehnika/akkumulyatory-i-akkumulyatornye-batarei"
parser.parsingcatalog1(urlq)
excel.SaveExcel()
parser.parsingcatalog(urlq)
excel.SaveExcel()