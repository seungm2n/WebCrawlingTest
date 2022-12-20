from bs import BeautifulSoup

html = open("fruits.html", "r", encoding="utf-8")
BeautifulSoup(html, "html.parse")