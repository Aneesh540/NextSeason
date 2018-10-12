import requests
import bs4 as bs 
import json
import urllib.request


def fetch_id(name):


    api = requests.get('http://www.omdbapi.com/?t={}&apikey=e7d8f97a'.format(name))
    print(api.status_code)
    json_format = api.json()

    print(json_format['imdbID'])
    print(json_format['Type'])
    print(json_format['Title'])
    print(json_format['Year'])

    return json_format['imdbID']

fetch_id("game of thrones")



def last_season():
    sauce = urllib.request.urlopen("https://www.imdb.com/title/tt2560140/?ref_=fn_al_tt_1").read()

    soup = bs.BeautifulSoup(sauce,'html.parser')

    inside = soup.findAll('div', class_ = 'seasons-and-year-nav')

    for div in inside: 
        link = div.findAll('a')
        for a in link:
            print(a.string,a.get('href'))

def last_episode(url):
    sauce = urllib.request.urlopen(url).read()

    soup = bs.BeautifulSoup(sauce, 'html.parser')

    inside = soup.findAll('div', class_ = 'airdate')

    last_list = []
    for div in inside:
        last_list.append(div.string.strip())

    print(last_list,sep="\n")       
         


# url = "https://www.imdb.com/title/tt2560140/episodes?season=3&ref_=tt_eps_sn_3"
# last_episode(url)
