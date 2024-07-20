import requests
from bs4 import BeautifulSoup

print("\n\nFederal Funds (effective) interest rates\n\n")

try:
    url = "https://www.federalreserve.gov/releases/h15/"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')

    tableHeaders = soup.find_all('th', limit=6)
    tableData = soup.find_all('td',limit=5)

    resultHeaders = []
    resultData = []

    for x in tableHeaders:
        resultHeaders.append(x.text)

    for x in tableData:
        resultData.append(x.text.replace("\xa0",""))

    for x in range(5):
        print(resultHeaders[x+1],":",resultData[x]+"%")

except ConnectionError:
    print("AT&T internet is being wacky again... *sigh*\n")

except KeyboardInterrupt:
    print("You stopped this from running!")
