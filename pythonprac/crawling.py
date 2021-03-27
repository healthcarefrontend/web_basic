import requests
from bs4 import BeautifulSoup

# 내가 받아온 것을, 솎아내는 것이 크롤링 {기술적으로 중요한 것은 1. 요청 2. 내가 원하는 정보를 잘 솎아내는 것}
# 요청하는 것은 requests, 솎아내는 것은 bs4
# headers 코드 단에서 사이트에 접속한 사이트들이 많음, 브라우저에서 사이트에서 접속한 효과를 내기위해 header를 씀
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    # print(a_tag)

    if a_tag is not None:
        print(a_tag.text)


# title = soup.select_one(
#     '#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')

# print(title['href'])  # /movie/bi/mi/basic.nhn?code=171539 속성을 가져옴
# # print(title.text) ## 그린북 안에 텍스트를 가지고 옴

# old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# old_content > table > tbody > tr:nth-child(3) > td.title > div > a

# old_content > table > tbody > tr:nth-child(2)
# old_content > table > tbody > tr:nth-child(3)

#old_content > table > tbody > tr
