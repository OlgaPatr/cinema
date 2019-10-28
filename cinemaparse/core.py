'''Cinema module'''
import requests
class CinemaParser:
    '''Class CinemaParser '''
    def __init__(self, town='msk'):
        '''Выбор города'''
        self.city = town
        self.content = []
    def extract_raw_content(self):
        '''Доставание информации со страницы'''
        inf = requests.get('https://{}.subscity.ru/'.format(self.city))
        self.content = inf.text
    def print_raw_content(self):
        '''Вывод информации со страницы'''
        soup = BeautifulSoup(self.content)
        print(soup.prettify())
SPB_PARSER = CinemaParser('spb')
SPB_PARSER.extract_raw_content()
SPB_PARSER.print_raw_content()
