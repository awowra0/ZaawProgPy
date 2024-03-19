import requests
import argparse
import zadania.Brawery


parser = argparse.ArgumentParser()
parser.add_argument('--city', default=None,
                    help='city filtering (default: None)')
args = parser.parse_args()


def fun_8(city=args.city):
    if city is None:
        link = 'https://api.openbrewerydb.org/'
        link = link + 'v1/breweries/random?size=20'
    else:
        link = 'https://api.openbrewerydb.org/v1/breweries?by_city='
        link = link + city.lower().strip() + '&per_page=20'
    print(link)
    f = requests.get(link)
    page = f.json()
    if (len(page) < 1 or 'message' in page and
       page['message'] == "Couldn't find Brewery"):
        print("Couldn't find Brewery")
        return
    for i in range(min(20, len(page))):
        i = zadania.Brawery([page[i][j] for j in page[i]])
        print(i)


if __name__ == '__main__':
    main()
