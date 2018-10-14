import config
import requests
import urllib
import bs4 as bs
import dating 

class ApiDetails:

    def __init__(self,tvseries):
        self.tvseries = tvseries
        api_url = config.API_KEY + tvseries
        self.key = requests.get(api_url).json()



    @property
    def response(self):
        return self.key['Response']

    @property
    def imdbID(self):
        return self.key['imdbID']

    @property
    def title(self):
        return self.key['Title']   

    @property
    def year(self):
        api_year = self.key['Year']
        api_year = api_year.split('-')

        
        return api_year

    @property
    def type(self):
        return self.key['Type']    
     

def fetchLastSeason(title):
    season_list = []
    url = "https://www.imdb.com/title/{}/?ref_=ttep_ep_tt".format(title)
    
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce,'html.parser')
    inside = soup.find_all('div', class_ = 'seasons-and-year-nav')

    for div in inside: 
        link = div.find('a')
        return link.string


def scrapeDates(title, season):

    last_list = []
    url = "https://www.imdb.com/title/{0}/episodes?season={1}".format(title,season)
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce, 'html.parser')

    inside = soup.findAll('div', class_ = 'airdate')
    
    
    for div in inside:
        last_list.append(div.string.strip())

    return last_list
    

def ListFormatter(date_list):

    if date_list[0] is '':
        return "CheckPrevious",-1

    penultimate = []
    for x in date_list:
        form = dating.compare_dates(x)
        penultimate.append(form)

    # print(penultimate)

    if penultimate[-1] is False:
        return "NoNextEpisode", 0 

    elif all(penultimate):
        return "CheckPrevious", date_list[0]   

    for i in range(len(penultimate)-1,0,-1):
        if penultimate[i] is True and penultimate[i-1] is False:
            print(date_list[i])
            return "Complete", date_list[i] 

    
               

      

if __name__ == "__main__":
    emp = ApiDetails("american horror story")
    last_season = fetchLastSeason(emp.imdbID)

    for seasons in range(int(last_season),0,-1):
        print("\n\nRunning Season = ",seasons,"-"*20,"\n\n")

        next_episode = scrapeDates(emp.imdbID,seasons)
        response, date = ListFormatter(next_episode)
        print(response,date)
        
        if response == "CheckPrevious" and date == -1:
            print("Kuch nahi mila")

        elif response == "Complete":
            print(date,"-----")
            break

        elif response == "CheckPrevious" and date != -1:
            # further possibility is there but we got a answer
            print("CHeck season 8")

        elif response == "NoNextEpisode":
            print("Series has finished ")
            break

        
    