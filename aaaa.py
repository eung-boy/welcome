#cd C:\Users\pvnrt\Anaconda3\Library\bin

from bs4 import BeautifulSoup #beautifulsoup 가져오기
import urllib.request #urlopen이 있는 것 가져오기
import re #정규식 가져오기

def get_soup(target_url): #targel url에서 parsing한 것들은 저장하는 함수
    html = urllib.request.urlopen(target_url).read() #urlopen함수를 사용해서 target url을 읽어온다
    soup = BeautifulSoup(html, 'html.parser') #읽어온 것을 beautifulsoup을 이용해서 parsing한다. 'html.parser'는 html을 parsing한다는 뜻인거 같다
    return soup # soup을 돌려준다. 즉, target url을 html코드를 parsing한것을 돌려주는 것이다.

def extract_data(soup):
    li1=[] #1 칼럼을 받을것
    li2=[] #2 칼럼을 받을것
    table = soup.find('table') #Table에 있는 code을 받는다. sigma-aldrich는 table 1개있음
    trs = table.find_all('tr') #tr로 있는 cod을 다 받는다.
    for idx, tr in enumerate(trs): #받은 tr값들을 받아서 진행하고, idx는 끝인걸 확인하는용도인듯..(잘모르겠다)
        if idx > 0:
            tds = tr.find_all('td') #tr내에 있는 td를 다 받고
            property = tds[0].text.strip() #첫째항은 bp mp등을 나타냄
            value = tds[1].text.strip() # 두째항은 값을 나타냄
            li1.append(property) #리스트로 만들어준다
            li2.append(value)
    if 'refractive index' in li1:  #refractive index가 있는 리스트의 index를 알아서 li2 에서 읽고싶다
        ind=li1.index('refractive index')
        x=li2[ind]
        y=list(x)  #n20/D 1.527 으로 나와서 index로 6~11이다
        print(''.join(y[6:11])) #list 6~11에 해당되는값들을 공백없이 붙여준다.
                                                        # rinumber=re.findall("\d+", '') 이건 정규식에서 이어지는 숫자를 찾는것임 왜인지는 모르겠는데 안됨
    if 'SMILES string'in li1: #smiles string이 있으면 그것도 읽어온다
        ind=li1.index('SMILES string')
        print(li2[ind])
    if 'SMILES' in li1: #smiles 가있으면 그것도 읽어온다
        ind=li1.index('SMILES')
        print(li2[ind])


target_url = 'https://www.sigmaaldrich.com/catalog/product/sigma/88640?lang=ko&region=KR'
soup = get_soup(target_url)
extract_data(soup)
