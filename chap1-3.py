## 텍스트 파일에 쓰기 : with문
## 'with as'로 파일 열고 '열었을 때 할 일'을 들여쓰면 됨 'close()' 쓰지 않아도 오류 발생x

import requests

url = "https://python.cyber.co.kr/pds/books/python2nd/test1.html"
response = requests.get(url)        #웹페이지를 구함

response.encoding = response.apparent_encoding  #글자 안 깨지도록 함

filename = "download.txt"
with open(filename, mode="w") as f:        # 파일 쓰기모드로 열기
    f.write(response.text)              # 인터넷에서 구한 데이터 쓰기
f.close()                           # 파일 닫기