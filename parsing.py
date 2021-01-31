from bs4 import BeautifulSoup as BS
import requests


def dev():
    for i in range(6):
        url = f"https://devkg.com/ru/jobs?page={i}"
        response = requests.get(url)
        soup = BS(response.content, "lxml")
        text = soup.find_all("div", class_="information")
        print(response)
        print(text)


if __name__ == "__main__":
    dev()