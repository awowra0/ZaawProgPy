import requests
import zadania.Brawery


def fun_7():
    link = 'https://api.openbrewerydb.org/v1/breweries/random?size=20'
    f = requests.get(link)
    page = f.json()
    for i in range(20):
        i = zadania.Brawery.Brawery([page[i][j] for j in page[i]])
        print(i)
