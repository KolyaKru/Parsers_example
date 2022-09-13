from classes import Parse, Excel

parser = Parse()
excel = Excel()

url = []

url.append("https://1ak.by/akkumulyatory/100-ah-alfa-hybrid-r")
url.append("https://1ak.by/akkumulyatory/100-ah-volta-r")
url.append("https://1ak.by/akkumulyatory/45-ah-topla-top-jis-r-118645")
url.append("https://1ak.by/akkumulyatory/95-ah-zver-l")
url.append("https://1ak.by/akkumulyatory/45-ah-545157033-627179-thomas-japan-l")

excel.CreateExcel()

for urlq in url:
    parser.parsingAkum(urlq)

excel.SaveExcel()