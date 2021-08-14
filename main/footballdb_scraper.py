from bs4 import BeautifulSoup
import requests
import re

def capture_from_url_ending_in(letter):
    url = 'https://www.footballdb.com/players/current.html?letter=' + letter.upper()

    page = requests.get(url, headers=headers).text
    soup = BeautifulSoup(page, 'lxml')
    divs = soup.find_all('div', {'class': 'td'})

    with open('rawfootball.txt', 'w') as file:
        file.write(str(divs))
    
    output = open('organizedfootball.txt', 'w')
    input = open('rawfootball.txt').read()

    # This regular expression performs the second pass, removing all data between and including the angled brackets.
    output.write(re.sub(r'\<(.*?)>.*?|]|\[', '', input))
    output.close()

# Custom headers to avoid error 403
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
