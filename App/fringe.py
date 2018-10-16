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
        the_date = div.string.strip()
        if the_date != '':
            last_list.append(the_date)

    return last_list
    

def ListFormatter(date_list):
    # print(date_list)

    if date_list[0] is '':
        # no airdate mentioned in website for episode
        return "CheckPrevious",-1

    penultimate = []
    for x in date_list:
        # True, False list of dates latest at last
        form = dating.compare_dates(x)
        penultimate.append(form)

    # print(penultimate)

    if penultimate[-1] is False:
        # latest episode is less then smallest date
        return "NoNextEpisode", 0 

    elif all(penultimate):
        # saare true hai, might be answer but check a list below 
        return "CheckPrevious", date_list[0]   

    for i in range(len(penultimate)-1,0,-1):
        if penultimate[i] is True and penultimate[i-1] is False:
            # print(date_list[i])
            return "Complete", date_list[i] 
      

def getNextEpisodeDate(mpa):

  
    emp = ApiDetails(mpa)
    last_season = fetchLastSeason(emp.imdbID)

    expected_date = ''

    for seasons in range(int(last_season),0,-1):
        # print("\n\nRunning Season = ",seasons,"-"*20,"\n\n")

        next_episode = scrapeDates(emp.imdbID,seasons)
        response, date = ListFormatter(next_episode)
       
        
        if response == "CheckPrevious" and date == -1:
            # print("Kuch nahi mila")
            pass

        elif response == "Complete":
            return dating.dateFormatter(date)
        

        elif response == "CheckPrevious" and date != -1:
            # further possibility is there but we got a answer for now
            # expected_date = date
            # print("till now = ", expected_date)
            pass
            


        elif response == "NoNextEpisode":
            # print("from this season = ",date)
            # print("from previous season = ",expected_date)

            if expected_date != '':
                return dating.dateFormatter(expected_date)
                

            return "The show has finished streaming all its episodes"
        

if __name__ == "__main__":
    mpa = input("Enter TV: ")
    print(getNextEpisodeDate(mpa))      
    