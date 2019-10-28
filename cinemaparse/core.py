import requests
from bs4 import BeautifulSoup

class CinemaParser:
  def __init__(self,town='msk'):
    self.city = town
  
  def extract_raw_content(self):
     inf = requests.get('https://{}.subscity.ru/'.format(self.city))
     self.content = inf.text
    
  def print_raw_content(self):
    soup = BeautifulSoup(self.content)
    print(soup.prettify())
    
spb_parser = CinemaParser('spb')
spb_parser.extract_raw_content()
spb_parser.print_raw_content()
#msk_parser = CinemaParser('msk')
#extract_raw_content()
#print_raw_content()
