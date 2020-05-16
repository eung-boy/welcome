#cd C:\Users\pvnrt\Anaconda3

from bs4 import BeautifulSoup #beautifulsoup 가져오기
import urllib.request #urlopen이 있는 것 가져오기

def get_soup(target_url): #targel url에서 parsing한 것들은 저장하는 함수
    html = urllib.request.urlopen(target_url).read() #urlopen함수를 사용해서 target url을 읽어온다
    soup = BeautifulSoup(html, 'html.parser') #읽어온 것을 beautifulsoup을 이용해서 parsing한다. 'html.parser'는 html을 parsing한다는 뜻인거 같다
    return soup # soup을 돌려준다. 즉, target url을 html코드를 parsing한것을 돌려주는 것이다.

def extract_data(soup):
    table = soup.find('table', {'class': 'infobox bordered'})
    trs = table.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        a=tds.text.strip()
        print(tds)

target_url = 'https://en.wikipedia.org/wiki/Thiophenol'
soup = get_soup(target_url)
extract_data(soup)
