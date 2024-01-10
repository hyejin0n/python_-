## 텍스트 파일에 쓰기: open, close
## 인터넷에 있는 HTML 파일을 읽어 들인 후 컴퓨터에 저장
import requests

url = "https://python.cyber.co.kr/pds/books/python2nd/test1.html"
response = requests.get(url)        #웹페이지를 구함

response.encoding = response.apparent_encoding  #글자 안 깨지도록 함

filename = "download.txt"
f = open(filename, mode="w")        # 파일 쓰기모드로 열기
f.write(response.text)              # 인터넷에서 구한 데이터 쓰기
f.close()                           # 파일 닫기