from bs4 import BeautifulSoup

if __name__ == '__main__':
    fp = open('./hhh.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'html.parser')
    print(soup)
