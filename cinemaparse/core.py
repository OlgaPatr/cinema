'''Cinema module'''
import requests
from bs4 import BeautifulSoup
class CinemaParser:
    '''Class CinemaParser '''
    def __init__(self, town='msk'):
        '''Выбор города'''
        self.city = town
        self.content = None
    def extract_raw_content(self):
        '''Доставание информации со страницы'''
        inf = requests.get('https://{}.subscity.ru/'.format(self.city))
        self.content = inf.text
    def print_raw_content(self):
        '''Вывод информации со страницы'''
        soup = BeautifulSoup(self.content)
        print(soup.prettify())

    def get_films_list(self):
        '''Достаёт названия фильмов со страницы'''
        soup = BeautifulSoup(self.content, 'html.parser')
        films = []
        for i in soup.find_all(class_="movie-plate"):
            films.append(i["attr-title"])
        print(films)
        return films

SPB_PARSER = CinemaParser('spb')
SPB_PARSER.extract_raw_content()
SPB_PARSER.get_films_list()
#SPB_PARSER.print_raw_content()
