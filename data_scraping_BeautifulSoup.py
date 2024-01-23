import requests
from bs4 import BeautifulSoup
import re


#Yahoo Newsのトップページ情報を取得
URL = "https://www.yahoo.co.jp/"
rest = requests.get(URL)

#BeautifulSoupにニュースのページ内容を読み込ませる
soup = BeautifulSoup(rest.text, "html.parser")

#ニュースの見出しとURLの情報を取得して出力する
data_list = soup.find_all(href = re.compile("news.yahoo.co.jp/pickup"))

for data in data_list:
  print(data.span.string)
  print(data.attrs["href"])
