from bs4 import BeautifulSoup
import requests

URL = "http://www.semyung.ac.kr/prog/vwBoard/bbs01/kor/sub08_02_01/list.do"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('div', class_="prog_content")
tds = table.find_all('tr')

for td in tds:
    title = td.findNext('a')
    date = td.findNext('td', class_='date')
    info = td.findNext(class_='problem_number')

    print(f"순번: {info.text.strip()}")
    print(f"공지 날짜: {date.text.strip()}")
    print(f"공지 제목: {title.text.strip()}")
    print()
