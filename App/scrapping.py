import requests
import config



def fetch_id(tvseries_name): 
    try:
        url = config.API_KEY + tvseries_name
        api_details = requests.get(url)
        api_details = api_details.json()
        
        response = api_details['Response']

    except:
        print("Check internet connection ")  

    else:      
        
        if response == "False":
            print("No such TV show exist on imdb")
            
            return None

        elif response == "True" and api_details['Type'] == "series":
            imdb_id = api_details['imdbID']
            year = api_details['Year']
            
            return (imdb_id,year)
        
        else:
            print("Enter TV series only, this is = ", api_details['Type'])
            return None

# def LastSeason(imdbID, year):
    
    





if __name__ == "__main__":

    for _ in range(10):
        tv_series = input("Enter TV series name: ")
        title = fetch_id(tv_series)
        
        if title != None:
            print(title)
            imdbID, year = title

            season = LastSeason(imdbID, year)
  
        
        
        elif title is None:
            pass
        
        else:
            print("checkpoint 1 NEVER GONNA HAPPEN")        



